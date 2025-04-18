
import numpy as np
import matplotlib.pyplot as plt
from gwpy.timeseries import TimeSeries
from scipy.signal import correlate, find_peaks

# Function definitions from previous steps
def generate_primary_signal(duration=1.0, fs=4096, f0=150, Q=10):
    t = np.linspace(0, duration, int(fs*duration), endpoint=False)
    envelope = np.exp(-t*f0/Q)
    signal = envelope * np.sin(2 * np.pi * f0 * t)
    return t, signal

def generate_echo(signal, delay, attenuation=0.2, fs=4096):
    echo = np.zeros_like(signal)
    sample_delay = int(delay * fs)
    if sample_delay < len(signal):
        echo[sample_delay:] = signal[:-sample_delay] * attenuation
    return echo

def matched_filter(data, template):
    template = template - np.mean(template)
    correlation = correlate(data, template, mode='same')
    return correlation / np.linalg.norm(template)

# Load GW150914 data from GWOSC
print("Downloading GW150914 strain data from LIGO Hanford (H1)...")
strain = TimeSeries.fetch_open_data('H1', 1126259462, 1126259462 + 4, sample_rate=4096)
strain = strain.crop(1126259462.5, 1126259463.5)  # Focus on region around merger

# Prepare echo signal
fs = 4096
t, signal = generate_primary_signal(duration=1.0, fs=fs)
echo = generate_echo(signal, delay=0.05, attenuation=0.3, fs=fs)
template = signal + echo

# Inject the signal into the real strain
data = strain.value.copy()
start = len(data) // 2
if start + len(signal) < len(data):
    data[start:start+len(signal)] += signal
    data[start:start+len(echo)] += echo

# Matched filter on real data
filtered = matched_filter(data, template)

# Peak detection
peaks, _ = find_peaks(filtered, height=np.max(filtered)*0.3, distance=fs*0.01)
if len(peaks) >= 2:
    primary_idx, echo_idx = peaks[0], peaks[1]
    echo_delay_samples = echo_idx - primary_idx
    echo_delay_sec = echo_delay_samples / fs
    print(f"Estimated echo delay: {echo_delay_sec:.5f} seconds (samples: {echo_delay_samples})")
else:
    print("Echo not clearly detected.")

# Plot
plt.figure(figsize=(10, 4))
plt.plot(filtered, label="Matched Filter Output")
if len(peaks) >= 1:
    plt.axvline(peaks[0], color='g', linestyle='--', label='Primary Peak')
if len(peaks) >= 2:
    plt.axvline(peaks[1], color='orange', linestyle='--', label='Echo Peak')
plt.axhline(np.max(filtered)*0.3, color='r', linestyle='--', label='Detection Threshold')
plt.legend()
plt.title("Matched Filter Echo Detection on GW150914 Strain Data (H1)")
plt.tight_layout()
plt.show()
