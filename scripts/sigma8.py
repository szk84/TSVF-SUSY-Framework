import numpy as np
import matplotlib.pyplot as plt

# Define wavenumber k (h/Mpc)
k = np.logspace(-2, 1, 500)  # 0.01 to 10 h/Mpc

# Standard GR matter power spectrum (mock model)
P_GR = k**(-3) * np.exp(-k)  # Roughly matches shape at z=0

# TSVF-SUSY suppression factor
lambda_star = 5.62  # Dimensionless UV fixed point
suppression_factor = 1 - 0.05 * (k/0.1)**0.5  # 5% suppression around k=0.1 h/Mpc

# Prevent negative suppression
suppression_factor = np.clip(suppression_factor, 0.7, 1.0)

# TSVF-SUSY suppressed spectrum
P_TSVF = P_GR * suppression_factor

# Plotting
plt.figure(figsize=(7,5))
plt.loglog(k, P_GR, '--', color='gray', label='Standard GR')
plt.loglog(k, P_TSVF, '-', color='navy', label='TSVF-SUSY Suppressed')

plt.xlabel(r'Wavenumber $k$ ($h/\mathrm{Mpc}$)', fontsize=12)
plt.ylabel(r'Matter Power Spectrum $P(k)$ (arb. units)', fontsize=12)
plt.title('Suppression of Matter Power Spectrum by TSVF-SUSY', fontsize=14)
plt.grid(True, which="both", linestyle="--", alpha=0.6)
plt.legend(fontsize=10)
plt.tight_layout()
plt.savefig('sigma8.png', dpi=300)
plt.close()
