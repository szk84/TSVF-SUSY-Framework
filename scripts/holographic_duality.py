import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(6,4))

# Draw bulk and boundary elements
ax.plot([0.2,0.8], [0.5,0.5], 'b-', lw=2)  # Bulk
ax.plot([0.2,0.8], [0.3,0.3], 'r--', lw=2)  # Boundary
ax.plot([0.5,0.5], [0.3,0.5], 'g-', lw=1)  # Connection

ax.text(0.5, 0.55, 'Bulk TSVF-SUSY', fontsize=12)
ax.text(0.5, 0.25, 'Boundary CFT', fontsize=12)
ax.set_xlim(0,1)
ax.set_ylim(0,1)
ax.axis('off')
plt.savefig('holographic_duality.png', dpi=300, bbox_inches='tight')
plt.close()