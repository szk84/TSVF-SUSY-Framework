import numpy as np
import matplotlib.pyplot as plt

# Constants
lmbda_tsvf = 5.62  # Corrected UV fixed point value
D_mpc = 100  # Distance in Megaparsecs
D = D_mpc * 3.086e22  # Convert Mpc to meters
M_p = 2.435e18  # Planck mass in GeV
hbar_c = 1.973e-16  # hbar * c in GeV*m

# Frequency range (10 Hz to 2000 Hz)
frequencies = np.linspace(10, 2000, 500)

# Phase shift calculation
def phase_shift(f, lmbda, D, M_p):
    f_gev = f * 4.1357e-15  # Convert Hz to GeV
    shift = 0.1 * (lmbda) * (f_gev / (1e-3))**3 * (D / (100 * 3.086e22))
    return shift

phase_shifts = phase_shift(frequencies, lmbda_tsvf, D, M_p)

# Plot
plt.figure(figsize=(8, 5))
plt.plot(frequencies, phase_shifts, label=r'$\tilde{\lambda}_{\mathrm{TSVF}}^* \approx 5.62$', color='blue')
plt.axhline(1e-7, color='red', linestyle='--', label='LISA Sensitivity Threshold')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Phase Shift $\Delta \\Phi_{GW}$ (radians)')
plt.title('Gravitational Wave Phase Shift vs Frequency (TSVF-SUSY)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('phase_shift_plot.png', dpi=300)
plt.show()
