import numpy as np
import matplotlib.pyplot as plt

f = np.logspace(-3, 1, 100)
h_TSVF = 1e-10 * (f/0.01)**(-0.5)
h_std = 5e-11 * (f/0.01)**(-0.7)

plt.figure(figsize=(6,4))
plt.loglog(f, h_TSVF, 'b-', lw=2, label='TSVF-SUSY')
plt.loglog(f, h_std, 'r--', lw=2, label='Standard')
plt.xlabel('Frequency (Hz)', fontsize=12)
plt.ylabel('Characteristic Strain', fontsize=12)
plt.legend()
plt.grid(True, which='both', alpha=0.3)
plt.savefig('phase_transition_gw.png', dpi=300, bbox_inches='tight')
plt.close()