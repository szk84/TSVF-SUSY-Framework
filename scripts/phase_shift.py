import numpy as np
import matplotlib.pyplot as plt

# Parameters
frequencies = np.logspace(1, 4, 100)  # 10 Hz to 10 kHz
lambda_tsvf = [1e-4, 5e-4, 1e-3]  # Coupling values
D = 100  # Distance in Mpc

# Phase shift formula
def delta_phi(f, lmbda):
    return 0.1 * (lmbda / 1e-4) * (f / 1e3)**3 * (D / 100)

# Plot
plt.figure(figsize=(10, 6))
for lmbda in lambda_tsvf:
    plt.plot(frequencies, delta_phi(frequencies, lmbda), 
             lw=2, label=fr'$\lambda = {lmbda:.1e}$')

plt.xscale('log')
plt.yscale('log')
plt.xlabel('Frequency (Hz)', fontsize=12)
plt.ylabel(r'$\Delta \Phi_{\rm GW}$', fontsize=12)
plt.title('Gravitational Wave Phase Shift', fontsize=14)
plt.legend()
plt.grid(alpha=0.3)
plt.savefig('phase_shift.png', dpi=300, bbox_inches='tight')
plt.close()