import numpy as np
import matplotlib.pyplot as plt

# Parameters
N = np.arange(10, 1001, 10)  # Number of D3-branes
V_w = 1e3  # Warped volume
Re_S = 1e2  # Dilaton-axion field

# Simplified relation: λ ~ N^2 / (V_w * sqrt(Re_S))
lambda_tsvf = (N**2) / (V_w * np.sqrt(Re_S))

# Plot
plt.figure(figsize=(10, 6))
plt.plot(N, lambda_tsvf, lw=2, color='purple')
plt.xlabel(r'Number of D3-Branes ($N$)', fontsize=12)
plt.ylabel(r'$\tilde{\lambda}_{\rm TSVF}/M_P^2$', fontsize=12)
plt.title('Holographic Parameter Matching', fontsize=14)
plt.grid(alpha=0.3)
plt.savefig('holographic_params.png', dpi=300, bbox_inches='tight')
plt.close()