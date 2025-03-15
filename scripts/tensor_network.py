import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(6,6))

# Draw tensor network elements
for i in range(5):
    ax.plot([0.2*i, 0.2*i+0.1], [0.5, 0.7], 'b-', lw=1)
    ax.plot([0.2*i, 0.2*i+0.1], [0.5, 0.3], 'r-', lw=1)

ax.text(0.5, 0.8, 'Forward', color='blue', fontsize=12)
ax.text(0.5, 0.2, 'Backward', color='red', fontsize=12)
ax.set_xlim(0,1)
ax.set_ylim(0,1)
ax.axis('off')
plt.savefig('tensor_network.png', dpi=300, bbox_inches='tight')
plt.close()