import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 0.1, 1000)
main_wave = np.exp(-100*(t-0.05)**2) * np.sin(100*np.pi*t)
echo = 0.3*np.exp(-150*(t-0.07)**2) * np.sin(100*np.pi*t)

plt.figure(figsize=(6,4))
plt.plot(t, main_wave, 'b-', lw=2, label='GR')
plt.plot(t, echo, 'r--', lw=2, label='Echo')
plt.xlabel('Time (s)', fontsize=12)
plt.ylabel('Strain', fontsize=12)
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig('echo.png', dpi=300, bbox_inches='tight')
plt.close()