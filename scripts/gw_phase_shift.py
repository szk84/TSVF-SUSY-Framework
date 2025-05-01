import numpy as np
import matplotlib.pyplot as plt

f = np.logspace(1, 4, 100)  # Frequency (Hz)
lambda_tsvf = 1.2e-4
D = 100  # Distance (Mpc)

delta_phi = 0.1 * (lambda_tsvf / 1e-4) * (f / 1e3)**3 * (D / 100)

plt.figure(figsize=(8, 6))
plt.loglog(f, delta_phi, lw=2, color='darkred')
plt.axvline(150, ls='--', color='gray', label='GW150914')
plt.xlabel('Frequency (Hz)', fontsize=12)
plt.ylabel(r'$\Delta\Phi_{\rm GW}$ (rad)', fontsize=12)
plt.title('Gravitational Wave Phase Shift')
plt.grid(alpha=0.3)
plt.legend()
plt.savefig('gw_phase_shift.png', dpi=300, bbox_inches='tight')