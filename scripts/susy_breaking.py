import numpy as np
import matplotlib.pyplot as plt

tsvf = np.linspace(0, 2e-4, 100)
m_soft = 1e3 * tsvf  # Example relation

plt.figure(figsize=(6,4))
plt.plot(tsvf, m_soft, 'b-', lw=2)
plt.xlabel(r'$\lambda_{TSVF}$', fontsize=12)
plt.ylabel('SUSY-breaking Scale (TeV)', fontsize=12)
plt.grid(True, alpha=0.3)
plt.savefig('susy_breaking.png', dpi=300, bbox_inches='tight')
plt.close()