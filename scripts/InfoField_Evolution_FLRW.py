import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Constants
lambda_info = 1e-2    # Coupling strength
M_P = 1.0             # Planck mass (set to 1 for natural units)
m = 1.0               # Mass parameter for V(I) = 0.5 * m^2 * I^2

# Ricci scalar R(t) in matter-dominated FLRW: R = 4 / (3t^2)
def R(t):
    return 4 / (3 * t**2)

# Derivative of potential: dV/dI = m^2 * I
def dV_dI(I):
    return m**2 * I

# Differential equation system for I(t): y = [I, dI/dt]
def dI_dt(t, y):
    I, dI = y
    H = 2 / (3 * t)  # Hubble parameter in matter-dominated FLRW
    d2I = -3 * H * dI - dV_dI(I) + (lambda_info / M_P**2) * R(t)
    return [dI, d2I]

# Time range and initial conditions
t_span = (0.1, 50)  # Avoid t=0 to prevent singularity
t_eval = np.linspace(*t_span, 1000)
y0 = [0.0, 0.0]     # Initial conditions: I(0), dI/dt(0)

# Solve the system
sol = solve_ivp(dI_dt, t_span, y0, t_eval=t_eval, method='RK45')

# Plot the solution
plt.figure(figsize=(10, 5))
plt.plot(sol.t, sol.y[0], label=r'$\mathcal{I}(t)$', color='indigo')
plt.title(r'Evolution of Informational Field $\mathcal{I}(t)$ in FLRW Background')
plt.xlabel('Time $t$')
plt.ylabel(r'$\mathcal{I}(t)$')
plt.grid(True)
plt.legend()
plt.tight_layout()

# Save the figure
plt.savefig("InfoField_Evolution_FLRW.png", dpi=300)
plt.show()
