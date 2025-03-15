import matplotlib.pyplot as plt
import matplotlib as mpl

# Set professional font settings
mpl.rcParams['font.family'] = 'DejaVu Sans'
mpl.rcParams['font.size'] = 12

# Create figure with two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Left Panel: Standard Hawking Radiation
ax1.set_title("Standard Hawking Radiation", pad=20)
ax1.plot([0.2, 0.8], [0.7, 0.3], 'r-', lw=2)
ax1.plot([0.2, 0.8], [0.3, 0.7], 'r-', lw=2)
ax1.text(0.5, 0.5, 'No correlations', rotation=45, 
        ha='center', va='center', color='maroon')

# Right Panel: TSVF-SUSY Correlation
ax2.set_title("TSVF-SUSY Correlation", pad=20)
ax2.plot([0.2, 0.8], [0.7, 0.3], 'b-', lw=2)
ax2.plot([0.2, 0.8], [0.3, 0.7], 'b-', lw=2)
ax2.plot([0.35, 0.65], [0.5, 0.5], 'g--', lw=3, alpha=0.7)
ax2.text(0.5, 0.45, 'Retrocausal\nentanglement', 
        ha='center', va='center', color='darkgreen')

# Common formatting
for ax in [ax1, ax2]:
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    
# Main title
plt.suptitle("Entanglement Structure of Hawking Radiation", 
            y=0.92, fontsize=14, fontweight='bold')

# Save figure
plt.tight_layout()
plt.savefig('entanglement_structure.png', dpi=300, 
           bbox_inches='tight', transparent=True)
plt.close()