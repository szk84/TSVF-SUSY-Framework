import numpy as np
import matplotlib.pyplot as plt

# TSVF-SUSY parameter (your defined test value)
lambda_TSVF = 1e-4
distance_Mpc = 400  # GW150914 actual approximate distance (~400 Mpc)

# Frequency range matching your ASD plot
freqs = np.linspace(10, 500, 1000)

# Compute TSVF-SUSY gravitational wave phase shift prediction
delta_phi_GW = 0.1 * (lambda_TSVF / 1e-4) * (freqs / 1e3)**3 * (distance_Mpc / 100)

# Compute quantum echo delay prediction
M_P_Hz = 2.435e42  # Planck mass in Hz
omega = 2 * np.pi * freqs
delta_t_echo = (lambda_TSVF * M_P_Hz) / omega**2

# Now overlay these clearly on your ASD plot
fig, ax1 = plt.subplots(figsize=(10, 6))

# Plot observed ASD clearly
ax1.loglog(asd.frequencies.value, asd.value, label='Observed GW150914 ASD', color='blue')

ax1.set_xlabel('Frequency [Hz]')
ax1.set_ylabel('Strain [Hz$^{-1/2}$]')
ax1.set_title('GW150914 ASD with TSVF-SUSY Predictions')

# Add TSVF-SUSY predicted phase shift on secondary axis
ax2 = ax1.twinx()
ax2.plot(freqs, delta_phi_GW, 'r--', label='TSVF-SUSY Phase Shift')
ax2.set_ylabel('Predicted Phase Shift (Radians)', color='red')
ax2.tick_params(axis='y', labelcolor='red')

fig.tight_layout()
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.show()
