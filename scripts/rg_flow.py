import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Define the beta function for λ_TSVF
def beta_func(ln_mu, lambda_val):
    beta = ((4 * np.pi**2) / 3) * lambda_val**3 * (1 - (5 * lambda_val**2) / (48 * np.pi**2))
    return beta

# Solve the RG equation: dλ/d(ln μ) = β(λ)
mu_range = np.logspace(np.log10(1e3), np.log10(1e19), 1000)  # Energy scale μ (GeV)
initial_lambda = 1e-4  # λ_TSVF at μ = 1 TeV

sol = solve_ivp(beta_func, 
                t_span=[np.log(1e3), np.log(1e19)], 
                y0=[initial_lambda], 
                t_eval=np.log(mu_range),
                method='RK45')

lambda_vals = sol.y[0]
mu_vals = np.exp(sol.t)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(mu_vals, lambda_vals, color='#2E86C1', linewidth=2.5)
plt.xscale('log')
plt.axhline(y=5.6, color='#E74C3C', linestyle='--', label=r'UV Fixed Point ($\lambda^* \approx 5.6$)')  # Fixed LaTeX
plt.xlabel('Energy Scale $\mu$ (GeV)', fontsize=12)
plt.ylabel(r'$\lambda_{\mathrm{TSVF}}$', fontsize=12)
plt.title(r'Renormalization Group Flow of $\lambda_{\mathrm{TSVF}}$', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()

# Save as .png
plt.savefig('rg_flow.png', dpi=300, bbox_inches='tight')
plt.close()