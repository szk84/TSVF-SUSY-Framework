import numpy as np
import matplotlib.pyplot as plt

# Example flow lines
tsvf = np.linspace(0, 8, 100)
beta = 0.1*tsvf**3 - 0.01*tsvf**5

plt.figure(figsize=(6,4))
plt.plot(tsvf, beta, 'b-', lw=2)
plt.axhline(0, color='k', linestyle='--')
plt.axvline(4*np.pi/np.sqrt(3), color='r', linestyle='--')
plt.xlabel(r'$\lambda_{TSVF}$', fontsize=12)
plt.ylabel(r'$\beta(\lambda_{TSVF})$', fontsize=12)
plt.grid(True, alpha=0.3)
plt.savefig('frg_flow.png', dpi=300, bbox_inches='tight')
plt.close()