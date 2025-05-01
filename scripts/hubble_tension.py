import numpy as np
import matplotlib.pyplot as plt

# Physical constants
H0_GR = 67.4  # Planck H0 (GR) in km/s/Mpc
lambda_ir = 1e-4  # IR value of dimensionless coupling
Omega_m = 0.315
Omega_Lambda = 0.685

# Redshift range
z = np.linspace(0, 2, 500)

# Standard GR Hubble parameter
H_GR = H0_GR * np.sqrt(Omega_m * (1 + z)**3 + Omega_Lambda)

# TSVF-SUSY corrected Hubble parameter (small increase)
H_TSVF = H0_GR * np.sqrt((Omega_m * (1 + z)**3 + Omega_Lambda) * (1 + lambda_ir))

# Fractional difference
delta_H = (H_TSVF - H_GR) / H_GR

# Plotting
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(7,8), sharex=True, gridspec_kw={'height_ratios': [3, 1]})

# Top plot: Hubble parameter evolution
ax1.plot(z, H_GR, '--', color='gray', label='Standard GR')
ax1.plot(z, H_TSVF, '-', color='blue', label='TSVF-SUSY Corrected')
ax1.set_ylabel(r'Hubble Parameter $H(z)$ (km/s/Mpc)', fontsize=12)
ax1.set_title('Hubble Parameter Evolution with TSVF-SUSY Corrections', fontsize=14)
ax1.grid(True, linestyle="--", alpha=0.6)
ax1.legend(fontsize=10)

# Bottom plot: Fractional difference
ax2.plot(z, delta_H*100, color='red', lw=2)
ax2.axhline(0, color='black', linestyle='--', lw=1)
ax2.set_xlabel('Redshift $z$', fontsize=12)
ax2.set_ylabel(r'$\Delta H/H$ (\%)', fontsize=12)
ax2.grid(True, linestyle="--", alpha=0.6)

plt.tight_layout()
plt.savefig('hubble_tension.png', dpi=300)
plt.close()
