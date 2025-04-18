
import numpy as np
import matplotlib.pyplot as plt

# Parameters
L = 16
beta = 1.0
lambda_TSVF = 0.01
v = 1.0
xi = 0.01
n_steps = 2000

# Fields
phi = np.random.normal(0, 0.1, (L, L))
R = np.random.normal(0, 0.01, (L, L))  # Dynamic curvature field

def action(phi, R):
    grad_sq = np.sum((np.roll(phi, 1, axis=0) - phi) ** 2)
    grad_sq += np.sum((np.roll(phi, 1, axis=1) - phi) ** 2)
    potential = lambda_TSVF * np.sum((phi**2 - v**2) ** 2)
    curvature_term = xi * np.sum(R * phi**2)
    return grad_sq + potential + curvature_term

def monte_carlo_step(phi, R, beta):
    for _ in range(L * L):
        # Update phi
        i, j = np.random.randint(0, L, size=2)
        old_phi = phi[i, j]
        new_phi = old_phi + np.random.normal(0, 0.1)
        phi_trial = phi.copy()
        phi_trial[i, j] = new_phi
        dS_phi = action(phi_trial, R) - action(phi, R)
        if dS_phi < 0 or np.random.rand() < np.exp(-beta * dS_phi):
            phi[i, j] = new_phi

        # Update R
        i, j = np.random.randint(0, L, size=2)
        old_R = R[i, j]
        new_R = old_R + np.random.normal(0, 0.01)
        R_trial = R.copy()
        R_trial[i, j] = new_R
        dS_R = action(phi, R_trial) - action(phi, R)
        if dS_R < 0 or np.random.rand() < np.exp(-beta * dS_R):
            R[i, j] = new_R

    return phi, R

def enforce_retrocausal(phi, R):
    phi[-1, :] = np.conj(phi[0, :])
    R[-1, :] = R[0, :]  # symmetric, not complex conjugate
    return phi, R

actions = []
for step in range(n_steps):
    phi, R = monte_carlo_step(phi, R, beta)
    phi, R = enforce_retrocausal(phi, R)
    if step % 100 == 0:
        actions.append(action(phi, R))

# Plot
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.imshow(np.real(phi), cmap='plasma', origin='lower')
plt.colorbar(label='Field Value')
plt.title('Final Field Configuration (Re[ϕ])')

plt.subplot(1, 2, 2)
plt.plot(actions)
plt.title('Action over Monte Carlo Steps')
plt.xlabel('Step (x100)')
plt.ylabel('Action S_E')

plt.tight_layout()
plt.show()
