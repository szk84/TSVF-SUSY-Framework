import numpy as np
import matplotlib.pyplot as plt

z = np.linspace(0, 3, 100)
H_early = 67 * (1 + z)**0.5
H_late = 74 * (1 + z)**0.4

plt.figure(figsize=(6,4))
plt.plot(z, H_early, 'b-', lw=2, label='Early Universe')
plt.plot(z, H_late, 'r--', lw=2, label='Late Universe')
plt.xlabel('Redshift (z)', fontsize=12)
plt.ylabel(r'$H(z)$ [km/s/Mpc]', fontsize=12)
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig('hubble.png', dpi=300, bbox_inches='tight')
plt.close()