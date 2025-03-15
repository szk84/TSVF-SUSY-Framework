import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(6,4))

# Forward path
ax.plot([0.2, 0.8], [0.2, 0.8], 'b-', lw=2)
ax.plot([0.8, 0.2], [0.8, 0.2], 'r-', lw=2)
ax.plot([0.5, 0.5], [0.5, 0.7], 'g--', lw=1)

ax.text(0.3, 0.3, 'Forward', color='blue', fontsize=12)
ax.text(0.6, 0.6, 'Backward', color='red', fontsize=12)
ax.text(0.45, 0.75, r'$\lambda_{TSVF}$', fontsize=14)

ax.set_xlim(0,1)
ax.set_ylim(0,1)
ax.axis('off')
plt.savefig('path_integral.png', dpi=300, bbox_inches='tight')
plt.close()