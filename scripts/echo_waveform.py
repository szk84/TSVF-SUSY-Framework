import numpy as np
import matplotlib.pyplot as plt

# Define time array
t = np.linspace(0, 0.2, 2000)  # 0 to 0.2 seconds

# Define a mock "GR waveform" (Gaussian modulated sinusoid)
f0 = 150  # Central GW frequency (Hz)
waveform_gr = np.sin(2*np.pi*f0*t) * np.exp(-((t-0.05)/0.01)**2)

# Echo parameters
echo_delay = 0.03  # 30 ms delay (based on retrocausal corrections)
echo_amplitude = 0.1  # Echo weaker by a factor of 10

# Create echo waveform
waveform_echo = np.sin(2*np.pi*f0*(t-echo_delay)) * np.exp(-((t-echo_delay-0.05)/0.01)**2)
waveform_echo[t < echo_delay] = 0  # Zero before echo time
waveform_total = waveform_gr + echo_amplitude * waveform_echo

# Plotting
plt.figure(figsize=(7,5))
plt.plot(t, waveform_total, label='Signal + Echo', color='blue', lw=2)
plt.plot(t, waveform_gr, '--', label='Original GR Signal', color='gray', alpha=0.7)
plt.axvline(x=echo_delay, color='red', linestyle='--', label=r'$\Delta t_{\text{echo}}$')
plt.xlabel('Time (s)', fontsize=12)
plt.ylabel('Amplitude (arbitrary units)', fontsize=12)
plt.title('Quantum Echo Waveform Prediction (TSVF-SUSY)', fontsize=14)
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend(fontsize=10)
plt.tight_layout()
plt.savefig('echo_waveform.png', dpi=300)
plt.close()
