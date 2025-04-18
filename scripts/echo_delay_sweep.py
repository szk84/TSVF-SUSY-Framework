
import numpy as np
import matplotlib.pyplot as plt
from gwpy.timeseries import TimeSeries
from scipy.signal import correlate

def generate_primary_signal(duration=1.0, fs=4096, f0=150, Q=10):
    t = np.linspace(0, duration, int(fs*duration), endpoint=False)
    envelope = np.exp(-t*f0/Q)
    signal = envelope * np.sin(2 * np.pi * f0 * t)
    return t, signal

def generate_echo(signal, delay, attenuation=0.3, fs=4096):
    echo = np.zeros_like(signal)
    sample_delay = int(delay * fs)
    if sample_delay < len(signal):
        echo[sample_delay:] = signal[:-sample_delay] * attenuation
    return echo

def inject_signal(strain, signal, echo):
    data = strain.copy()
    midpoint = len(data) // 2
    end = midpoint + len(signal)
    if end <= len(data):
        data[midpoint:end] += signal
        data[midpoint:end] += echo
    return data

def matched_filter(data, template):
    template = template - np.mean(template)
    correlation = correlate(data, template, mode='same')
    return correlation / np.linalg.norm(template)

# Load longer real GW150914 strain data (Hanford)
print("Loading real strain data...")
strain = TimeSeries.fetch_open_data('H1', 1126259462, 1126259462 + 6, sample_rate=4096)
strain = strain.crop(1126259463, 1126259465).value  # full 2 seconds

# Base signal
fs = 4096
t, signal = generate_primary_signal(duration=1.0, fs=fs)

# Sweep delays
delays = np.linspace(0.01, 0.12, 25)  # from 10ms to 120ms
snrs = []

for delay in delays:
    echo = generate_echo(signal, delay=delay, attenuation=0.3, fs=fs)
    injected = inject_signal(strain, signal, echo)
    template = signal + echo
    filtered = matched_filter(injected, template)
    snr = np.max(filtered) / np.std(strain)
    snrs.append(snr)

# Plot SNR vs Echo Delay
plt.figure(figsize=(8, 5))
plt.plot(delays * 1000, snrs, marker='o')
plt.xlabel("Echo Delay (ms)")
plt.ylabel("Matched Filter Peak SNR")
plt.title("Echo Detectability Curve in GW150914 (H1)")
plt.grid(True)
plt.tight_layout()
plt.show()
