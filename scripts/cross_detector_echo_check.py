
import numpy as np
import matplotlib.pyplot as plt
from gwpy.timeseries import TimeSeries
from scipy.signal import correlate, find_peaks

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

# Load GW150914 strain data from both H1 and L1
print("Loading H1 and L1 data for GW150914...")
strain_H1 = TimeSeries.fetch_open_data('H1', 1126259462, 1126259462 + 6, sample_rate=4096).crop(1126259463, 1126259465).value
strain_L1 = TimeSeries.fetch_open_data('L1', 1126259462, 1126259462 + 6, sample_rate=4096).crop(1126259463, 1126259465).value

# Generate signal and echo
fs = 4096
t, signal = generate_primary_signal(duration=1.0, fs=fs)
echo = generate_echo(signal, delay=0.05, attenuation=0.3, fs=fs)
template = signal + echo

# Inject into both detectors
data_H1 = inject_signal(strain_H1, signal, echo)
data_L1 = inject_signal(strain_L1, signal, echo)

# Matched filtering
filtered_H1 = matched_filter(data_H1, template)
filtered_L1 = matched_filter(data_L1, template)

# Peak detection
peaks_H1, _ = find_peaks(filtered_H1, height=np.max(filtered_H1)*0.3, distance=fs*0.01)
peaks_L1, _ = find_peaks(filtered_L1, height=np.max(filtered_L1)*0.3, distance=fs*0.01)

# Estimate echo delay in both detectors
if len(peaks_H1) >= 2 and len(peaks_L1) >= 2:
    delay_H1 = (peaks_H1[1] - peaks_H1[0]) / fs
    delay_L1 = (peaks_L1[1] - peaks_L1[0]) / fs
    print(f"H1 Echo Delay: {delay_H1:.5f} sec, L1 Echo Delay: {delay_L1:.5f} sec")
else:
    print("Could not find two clear peaks in both detectors.")

# Plot
plt.figure(figsize=(12, 5))
plt.subplot(2, 1, 1)
plt.plot(filtered_H1, label='H1 Matched Filter Output')
for pk in peaks_H1[:2]:
    plt.axvline(pk, color='g' if pk == peaks_H1[0] else 'orange', linestyle='--')
plt.title('H1 Echo Detection')
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(filtered_L1, label='L1 Matched Filter Output')
for pk in peaks_L1[:2]:
    plt.axvline(pk, color='g' if pk == peaks_L1[0] else 'orange', linestyle='--')
plt.title('L1 Echo Detection')
plt.legend()

plt.tight_layout()
plt.show()
