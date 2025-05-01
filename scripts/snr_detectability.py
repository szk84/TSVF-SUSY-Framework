import numpy as np
import matplotlib.pyplot as plt

# Parameters
lambda_tsvf = np.logspace(-6, -3, 100)  # 1e-6 to 1e-3

# SNR formula (simplified)
def snr(lmbda, detector_sensitivity):
    return detector_sensitivity * lmbda / 1e-4

# Plot
plt.figure(figsize=(10, 6))
plt.plot(lambda_tsvf, snr(lambda_tsvf, 8.2), lw=2, label='Einstein Telescope')
plt.plot(lambda_tsvf, snr(lambda_tsvf, 0.5), lw=2, label='LISA')
plt.xscale('log')
plt.xlabel(r'$\tilde{\lambda}_{\rm TSVF}$', fontsize=12)
plt.ylabel('SNR', fontsize=12)
plt.title('Signal-to-Noise Ratio vs. Coupling Strength', fontsize=14)
plt.legend()
plt.grid(alpha=0.3)
plt.savefig('snr_detectability.png', dpi=300, bbox_inches='tight')
plt.close()