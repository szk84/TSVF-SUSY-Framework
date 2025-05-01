import numpy as np
import matplotlib.pyplot as plt

# Constants
M_P = 1.22e19  # Planck mass in GeV (natural units)
lambda_TSVF = 5.62  # UV fixed point value from TSVF-SUSY

# Frequency range (in Hz)
frequencies = np.linspace(10, 2000, 500)  # LIGO/LISA range
omega = 2 * np.pi * frequencies  # Convert to angular frequency (rad/s)

# Corrected Echo Delay Formula:
# Δt_echo ∝ (1 / lambda_TSVF) * (M_P^2 / omega^3)
echo_delay = (1 / lambda_TSVF) * (M_P**2 / omega**3)

# Normalize for visual scaling
echo_delay_normalized = echo_delay / np.max(echo_delay)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(frequencies, echo_delay_normalized, color='blue', linewidth=2,
         label=r'$\Delta t_{\mathrm{echo}} \propto \frac{1}{\lambda_{\mathrm{TSVF}}} \cdot \frac{M_P^2}{\omega^3}$')
plt.xlabel('Gravitational Wave Frequency (Hz)', fontsize=12)
plt.ylabel('Normalized Echo Delay', fontsize=12)
plt.title('Quantum Echo Delay vs Gravitational Wave Frequency', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.tight_layout()
plt.savefig("echo_delay.png", dpi=300)
plt.show()
