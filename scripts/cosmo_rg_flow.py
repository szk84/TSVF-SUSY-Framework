import numpy as np
import matplotlib.pyplot as plt

# Define the RG flow beta function for dimensionless coupling
def beta_lambda(lmbda):
    return -2 * lmbda + (4 * np.pi)**2 / 3 * lmbda**3 * (1 - 5 * lmbda / (48 * np.pi**2))

# Setup RG scale (logarithmic range) focusing on cosmological scales
log_k = np.linspace(np.log10(1e-33), np.log10(1e3), 2000)  # From Hubble scale (~10^-33 GeV) to ~1 TeV
k = 10**log_k

# Initialize coupling array
lambda_flow = np.zeros_like(k)
lambda_flow[0] = 5.62  # Start from UV fixed point

# RK2 integration (midpoint method)
for i in range(1, len(k)):
    dlogk = np.log(k[i] / k[i-1])
    mid_lambda = lambda_flow[i-1] + 0.5 * beta_lambda(lambda_flow[i-1]) * dlogk
    lambda_flow[i] = lambda_flow[i-1] + beta_lambda(mid_lambda) * dlogk

# Plotting
plt.figure(figsize=(7,5))
plt.plot(log_k, lambda_flow, label=r'$\tilde{\lambda}_{\mathrm{TSVF}}(k)$', color='darkgreen', lw=2)

# Mark IR fixed point approximate region
plt.axhline(1e-4, color='lightblue', linestyle='--', label=r'IR limit $\sim 10^{-4}$')

plt.xlabel(r'$\log_{10}(k/\mathrm{GeV})$', fontsize=12)
plt.ylabel(r'$\tilde{\lambda}_{\mathrm{TSVF}}$', fontsize=12)
plt.title('Cosmological RG Flow of $\tilde{\lambda}_{\mathrm{TSVF}}$', fontsize=14)
plt.xlim([-33, 3])
plt.ylim([0, 6])
plt.grid(True, which='both', linestyle='--', alpha=0.6)
plt.legend(fontsize=10)
plt.tight_layout()
plt.savefig('cosmo_rg_flow.png', dpi=300)  # Save with new filename
plt.close()
