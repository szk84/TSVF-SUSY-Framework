import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-0.5, 0.5, 200)
gr_wave = np.exp(-t**2/0.01) * np.cos(40*t)
tsvf_wave = gr_wave * (1 + 0.1*np.sin(80*t))

plt.figure(figsize=(6,4))
plt.plot(t, gr_wave, 'b-', lw=2, label='GR')
plt.plot(t, tsvf_wave, 'orange', lw=2, label='TSVF-SUSY')
plt.xlabel('Time (s)', fontsize=12)
plt.ylabel('Normalized Strain', fontsize=12)
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig('waveform_deviation.png', dpi=300, bbox_inches='tight')
plt.close()