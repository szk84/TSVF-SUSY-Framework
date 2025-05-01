import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Define the beta function (dimensionless)
def beta_func(lmbda, _):
    lmbda_star = 5.62  # UV fixed point
    term1 = -2 * lmbda
    term2 = (4 * np.pi**2 / 3) * lmbda**3 * (1 - 5 * lmbda / (48 * np.pi**2))
    return term1 + term2

# Solve the RG equation: dλ/dlnk = β(λ)
k_log = np.linspace(0, 40, 1000)  # ln(k/M_P)
lmbda_0 = 5.62  # Initial condition at k = M_P
sol = odeint(beta_func, lmbda_0, k_log)
lmbda = sol[:, 0]

# Convert ln(k/M_P) to energy scale labels
energy_scales = {
    0: r'$k = M_P$ (Planck)',
    10: r'$k = 10^{16}$ GeV (GUT)',
    23: r'$k = 1$ TeV (LHC)',
    40: r'$k = 10^{-12}$ GeV (LIGO)'
}

# Plot
plt.figure(figsize=(10, 6))
plt.plot(k_log, lmbda, lw=2, color='navy')
plt.xlabel(r'$\ln(k/M_P)$', fontsize=12)
plt.ylabel(r'$\tilde{\lambda}_{\rm TSVF}(k)$', fontsize=12)
plt.title('RG Flow of the Retrocausal Coupling', fontsize=14)
plt.grid(alpha=0.3)

# Add energy scale annotations
for pos, label in energy_scales.items():
    plt.axvline(pos, color='gray', ls='--', alpha=0.5)
    plt.text(pos, 5.5, label, rotation=90, va='top', ha='right', fontsize=9)

# Save
plt.savefig('rg_flow.png', dpi=300, bbox_inches='tight')
plt.close()

# Generate table
table_data = [
    ["Energy Scale", r"$\tilde{\lambda}_{\rm TSVF}(k)$"],
    ["Planck ($M_P$)", f"{lmbda[0]:.2f}"],
    ["GUT ($10^{16}$ GeV)", f"{np.interp(10, k_log, lmbda):.2e}"],
    ["LHC (1 TeV)", f"{np.interp(23, k_log, lmbda):.2e}"],
    ["LIGO ($10^{-12}$ GeV)", f"{np.interp(40, k_log, lmbda):.2e}"]
]

print("\n".join(["| "+" | ".join(row)+" |" for row in table_data]))