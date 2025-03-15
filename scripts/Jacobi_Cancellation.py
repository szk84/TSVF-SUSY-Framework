import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib import rcParams

# Configure fonts for LaTeX compatibility
rcParams['font.family'] = 'serif'
rcParams['text.usetex'] = True

fig, ax = plt.subplots(figsize=(10, 6))

# --- Diagram Elements ---
# Gravitino contributions
gravitino = patches.Ellipse((0.3, 0.6), 0.2, 0.15, fc='skyblue', ec='navy', lw=2)
ax.add_patch(gravitino)
plt.text(0.3, 0.6, r"Gravitino $\psi_\mu^\omega$", ha='center', va='center', fontsize=12)

# Ricci tensor terms
ricci = patches.FancyBboxPatch((0.6, 0.6), 0.25, 0.15, boxstyle="round,pad=0.02",
                              fc='lightcoral', ec='darkred', lw=2)
ax.add_patch(ricci)
plt.text(0.6, 0.6, r"Ricci Terms: $\nabla_\mu R$", ha='center', va='center', fontsize=12)

# Cancellation mechanism
cancel_zone = patches.Wedge((0.45, 0.3), 0.25, 225, 315, fc='lightgreen', ec='darkgreen', alpha=0.4)
ax.add_patch(cancel_zone)
plt.text(0.45, 0.25, r"$\nabla^\mu G_{\mu\nu} = 0$ (Bianchi Identity)", 
         ha='center', va='center', fontsize=14, color='darkgreen')

# Mathematical foundation box
math_box = patches.FancyBboxPatch((0.1, 0.1), 0.8, 0.15, boxstyle="round,pad=0.05",
                                 fc='lightyellow', ec='goldenrod', lw=2)
ax.add_patch(math_box)
plt.text(0.5, 0.15, 
         r"Jacobi Identity: $\{Q_\alpha, \{Q_\beta, \bar{Q}_{\dot{\alpha}}\}\} + \text{cyclic} = 0$",
         ha='center', va='center', fontsize=12)

# --- Arrows and Annotations ---
# Gravitino to cancellation
ax.annotate('', xy=(0.4, 0.5), xytext=(0.3, 0.52),
            arrowprops=dict(arrowstyle='->', lw=1.5, color='navy'))

# Ricci to cancellation
ax.annotate('', xy=(0.55, 0.5), xytext=(0.6, 0.52),
            arrowprops=dict(arrowstyle='->', lw=1.5, color='darkred'))

# Cancellation result
ax.annotate(r'$\Rightarrow \text{Closure}$', xy=(0.45, 0.4), xytext=(0.45, 0.45),
            ha='center', va='bottom', fontsize=14, color='darkgreen',
            arrowprops=dict(arrowstyle='->', color='darkgreen'))

# --- Formatting ---
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')
plt.title(r"\textbf{Jacobi Identity Closure Mechanism in TSVF-SUSY}", y=0.95, fontsize=16)

# Save high-resolution version
plt.savefig('Jacobi_Cancellation.png', dpi=600, bbox_inches='tight', transparent=True)
plt.close()