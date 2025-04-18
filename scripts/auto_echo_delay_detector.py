
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import correlate, find_peaks
from scipy.stats import norm

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

def inject_signal(noise, main_signal, echo_signal):
    injected = noise.copy()
    midpoint = len(noise) // 2
    injected[midpoint:midpoint+len(main_signal)] += main_signal
    injected[midpoint:midpoint+len(echo_signal)] += echo_signal
    return injected

def matched_filter(data, template):
    template = template - np.mean(template)
    correlation = correlate(data, template, mode='same')
    return correlation / np.linalg.norm(template)

def estimate_snr(correlation, data_std):
    peak = np.max(correlation)
    snr = peak / data_std
    return snr

# Simulation parameters
fs = 4096
duration = 1.0
t, signal = generate_primary_signal(duration, fs)
echo = generate_echo(signal, delay=0.05, attenuation=0.2, fs=fs)
template_combined = signal + echo

# Noise and injection
noise = np.random.normal(0, 1e-21, int(fs*duration*2))
data = inject_signal(noise, signal, echo)

# Matched filtering
corr_combined = matched_filter(data, template_combined)

# Automatic peak detection to estimate echo delay
peaks, _ = find_peaks(corr_combined, height=np.max(corr_combined)*0.3, distance=fs*0.01)
if len(peaks) >= 2:
    primary_index = peaks[0]
    echo_index = peaks[1]
    echo_delay_samples = echo_index - primary_index
    echo_delay_sec = echo_delay_samples / fs
    print(f"Estimated echo delay: {echo_delay_sec:.5f} seconds (samples: {echo_delay_samples})")
else:
    echo_delay_sec = None
    print("Could not detect a distinct echo peak.")

# Plotting
plt.figure(figsize=(10, 4))
plt.plot(corr_combined, label='Matched Filter Output (Combined)')
plt.axvline(peaks[0], color='g', linestyle='--', label='Primary Peak')
if len(peaks) > 1:
    plt.axvline(peaks[1], color='orange', linestyle='--', label='Echo Peak')
plt.axhline(np.max(corr_combined)*0.3, color='r', linestyle='--', label='Peak Detection Threshold')
plt.title("Automatic Echo Detection from Matched Filter Output")
plt.legend()
plt.tight_layout()
plt.show()
