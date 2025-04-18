
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

# Matched filters
corr_primary = matched_filter(data, signal)
corr_echo = matched_filter(data, echo)
corr_combined = matched_filter(data, template_combined)

# SNR Estimation
data_std = np.std(noise)
snr_primary = estimate_snr(corr_primary, data_std)
snr_echo = estimate_snr(corr_echo, data_std)
snr_combined = estimate_snr(corr_combined, data_std)

# Bayesian-style confidence (simplified)
def confidence_level(snr, threshold=5.0):
    return norm.cdf(snr - threshold)

conf_primary = confidence_level(snr_primary)
conf_echo = confidence_level(snr_echo)

# Plotting
plt.figure(figsize=(12, 8))
plt.subplot(3, 1, 1)
plt.plot(corr_primary, label=f'Primary Signal Match (SNR={snr_primary:.2f})')
plt.legend()

plt.subplot(3, 1, 2)
plt.plot(corr_echo, label=f'Echo Match (SNR={snr_echo:.2f}, Confidence={conf_echo:.2%})')
plt.legend()

plt.subplot(3, 1, 3)
plt.plot(corr_combined, label=f'Combined Match (SNR={snr_combined:.2f})')
plt.axhline(np.max(corr_combined)*0.6, color='r', linestyle='--', label='Detection Threshold')
plt.legend()

plt.tight_layout()
plt.show()
