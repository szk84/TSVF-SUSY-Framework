
import numpy as np
import matplotlib.pyplot as plt
from gwpy.timeseries import TimeSeries
from scipy.signal import correlate

def generate_primary_signal(duration=1.0, fs=4096, f0=300, Q=15):
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

# Load GW170817 strain data (Hanford)
print("Loading GW170817 strain data (H1)...")
strain = TimeSeries.fetch_open_data('H1', 1187008882, 1187008882 + 6, sample_rate=4096)
strain = strain.crop(1187008883, 1187008885).value  # 2-second window around merger

# Base signal (neutron star merger: higher freq and shorter Q)
fs = 4096
t, signal = generate_primary_signal(duration=1.0, fs=fs)

# Sweep echo delays
delays = np.linspace(0.01, 0.12, 25)
snrs = []

for delay in delays:
    echo = generate_echo(signal, delay=delay, attenuation=0.3, fs=fs)
    injected = inject_signal(strain, signal, echo)
    template = signal + echo
    filtered = matched_filter(injected, template)
    snr = np.max(filtered) / np.std(strain)
    snrs.append(snr)

# Plot
plt.figure(figsize=(8, 5))
plt.plot(delays * 1000, snrs, marker='o')
plt.xlabel("Echo Delay (ms)")
plt.ylabel("Matched Filter Peak SNR")
plt.title("Echo Detectability Curve in GW170817 (H1)")
plt.grid(True)
plt.tight_layout()
plt.show()
