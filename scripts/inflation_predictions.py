import numpy as np
import matplotlib.pyplot as plt

n_s = np.linspace(0.94, 1.0, 100)
r_TSVF = 0.001 * np.ones_like(n_s)
r_Starobinsky = 0.003 * (1 - (n_s-0.965)/0.01)

plt.figure(figsize=(6,4))
plt.plot(n_s, r_TSVF, 'b-', lw=2, label='TSVF-SUSY')
plt.plot(n_s, r_Starobinsky, 'r--', lw=2, label='Starobinsky')
plt.xlabel(r'$n_s$', fontsize=14)
plt.ylabel(r'$r$', fontsize=14)
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig('inflation_predictions.png', dpi=300, bbox_inches='tight')
plt.close()