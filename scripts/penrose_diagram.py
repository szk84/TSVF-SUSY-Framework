import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(6,6))

# Draw Penrose diagram elements
ax.plot([0,1], [0,1], 'k-', lw=2)  # Diagonal
ax.plot([0,1], [1,0], 'k-', lw=2)  # Other diagonal
ax.plot([0.4,0.6], [0.6,0.4], 'r--', lw=1)  # Retrocausal path

ax.text(0.5, 0.3, r'$\lambda_{TSVF}$', fontsize=14, rotation=45)
ax.set_xlim(0,1)
ax.set_ylim(0,1)
ax.axis('off')
plt.savefig('penrose_diagram.png', dpi=300, bbox_inches='tight')
plt.close()