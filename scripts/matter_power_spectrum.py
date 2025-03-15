import numpy as np
import matplotlib.pyplot as plt

k = np.logspace(-2, 1, 100)
P_LCDM = k**0.9
P_TSVF = P_LCDM * (1 - 0.05*(k/0.5)**2)

plt.figure(figsize=(6,4))
plt.loglog(k, P_LCDM, 'r-', lw=2, label=r'$\Lambda$CDM')
plt.loglog(k, P_TSVF, 'b-', lw=2, label='TSVF-SUSY')
plt.xlabel(r'$k$ [h/Mpc]', fontsize=12)
plt.ylabel(r'$P(k)$', fontsize=14)
plt.legend()
plt.grid(True, which='both', alpha=0.3)
plt.savefig('matter_power.png', dpi=300, bbox_inches='tight')
plt.close()