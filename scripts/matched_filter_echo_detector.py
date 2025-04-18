
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import correlate, find_peaks
from scipy.signal.windows import tukey

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

def inject_signal_with_echo(noise, signal, echo):
    combined = noise.copy()
    midpoint = len(noise) // 2
    combined[midpoint:midpoint+len(signal)] += signal
    combined[midpoint:midpoint+len(echo)] += echo
    return combined

def matched_filter(data, template):
    correlation = correlate(data, template, mode='same')
    return correlation / np.linalg.norm(template)

# Parameters
fs = 4096
duration = 1.0
noise = np.random.normal(0, 1e-21, int(fs*duration*2))  # Simulated detector noise

# Generate main signal and echo
t, signal = generate_primary_signal(duration, fs)
echo = generate_echo(signal, delay=0.05, attenuation=0.2, fs=fs)

# Inject into noise
data = inject_signal_with_echo(noise, signal, echo)

# Matched filtering
template = signal + generate_echo(signal, delay=0.05, attenuation=0.2, fs=fs)
filtered = matched_filter(data, template)

# Plotting
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(data, label='Noisy Data with Signal + Echo')
plt.legend()
plt.subplot(2, 1, 2)
plt.plot(filtered, label='Matched Filter Output')
plt.axhline(np.max(filtered)*0.6, color='r', linestyle='--', label='Detection Threshold')
plt.legend()
plt.tight_layout()
plt.show()
