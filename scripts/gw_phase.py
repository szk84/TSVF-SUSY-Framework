import numpy as np
import matplotlib.pyplot as plt

f = np.linspace(10, 2000, 100)
phase_GR = 0.1*(f/1000)**3
phase_TSVF = phase_GR * 1.2  # Example modification

plt.figure(figsize=(6,4))
plt.plot(f, phase_GR, 'b-', lw=2, label='GR')
plt.plot(f, phase_TSVF, 'r--', lw=2, label='TSVF-SUSY')
plt.xlabel('Frequency (Hz)', fontsize=12)
plt.ylabel(r'$\Delta\Phi_{GW}$', fontsize=14)
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig('gw_phase.png', dpi=300, bbox_inches='tight')
plt.close()