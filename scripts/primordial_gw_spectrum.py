import numpy as np
import matplotlib.pyplot as plt

f = np.logspace(-18, 2, 100)
Ω_TSVF = 1e-15 * (f/1e-3)**0.5
Ω_Starobinsky = 1e-16 * (f/1e-3)**(-0.1)

plt.figure(figsize=(6,4))
plt.loglog(f, Ω_TSVF, 'b-', lw=2, label='TSVF-SUSY')
plt.loglog(f, Ω_Starobinsky, 'r--', lw=2, label='Starobinsky')
plt.xlabel('Frequency (Hz)', fontsize=12)
plt.ylabel(r'$\Omega_{GW}$', fontsize=14)
plt.legend()
plt.grid(True, which='both', alpha=0.3)
plt.savefig('primordial_gw_spectrum.png', dpi=300, bbox_inches='tight')
plt.close()