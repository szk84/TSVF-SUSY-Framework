
import numpy as np
import matplotlib.pyplot as plt
from gwpy.timeseries import TimeSeries
from scipy.signal import correlate, find_peaks

def generate_primary_signal(duration=1.0, fs=4096, f0=150, Q=10):
    t = np.linspace(0, duration, int(fs * duration), endpoint=False)
    envelope = np.exp(-t * f0 / Q)
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

# Load GW150914 H1 data
strain = TimeSeries.fetch_open_data('H1', 1126259462, 1126259462 + 6, sample_rate=4096).crop(1126259463, 1126259465).value

# Generate signal and echo
fs = 4096
t, signal = generate_primary_signal(duration=1.0, fs=fs)
echo = generate_echo(signal, delay=0.05, attenuation=0.3, fs=fs)
template = signal + echo

# Inject into real data
injected = inject_signal(strain, signal, echo)
filtered = matched_filter(injected, template)
true_snr = np.max(filtered) / np.std(strain)
print(f"Actual injected SNR: {true_snr:.3f}")

# Bootstrap simulation
n_trials = 200
boot_snrs = []

for i in range(n_trials):
    noise_sample = np.random.permutation(strain)
    filtered_noise = matched_filter(noise_sample, template)
    peak = np.max(filtered_noise)
    snr = peak / np.std(noise_sample)
    boot_snrs.append(snr)

# Compute stats
boot_snrs = np.array(boot_snrs)
mean_boot = np.mean(boot_snrs)
std_boot = np.std(boot_snrs)
z_score = (true_snr - mean_boot) / std_boot

print(f"Bootstrap Mean SNR: {mean_boot:.3f}")
print(f"Bootstrap StdDev: {std_boot:.3f}")
print(f"Z-score of actual detection: {z_score:.2f}")

# Plot histogram
plt.figure(figsize=(8, 5))
plt.hist(boot_snrs, bins=30, alpha=0.7, label='Bootstrap SNRs')
plt.axvline(true_snr, color='r', linestyle='--', label='Injected Echo SNR')
plt.xlabel("Matched Filter SNR")
plt.ylabel("Frequency")
plt.title("Bootstrap Confidence Estimation for Echo Detection")
plt.legend()
plt.tight_layout()
plt.show()
