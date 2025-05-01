import numpy as np
import matplotlib.pyplot as plt

# Constants
M_P = 1.22e19  # Planck mass in GeV
lambda_tsvf = 1e-4

# Echo delay formula
def delta_t(f):
    omega = 2 * np.pi * f
    return (lambda_tsvf * M_P**2) / omega**3

# Frequencies
frequencies = np.logspace(1, 3, 100)  # 10 Hz to 1 kHz

# Plot
plt.figure(figsize=(10, 6))
plt.plot(frequencies, delta_t(frequencies), lw=2, color='darkred')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Frequency (Hz)', fontsize=12)
plt.ylabel(r'$\Delta t_{\rm echo}$ (s)', fontsize=12)
plt.title('Quantum Echo Delay', fontsize=14)
plt.grid(alpha=0.3)
plt.savefig('echo_delay.png', dpi=300, bbox_inches='tight')
plt.close()