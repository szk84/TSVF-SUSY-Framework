
import numpy as np
import matplotlib.pyplot as plt

# Parameters
L = 16
beta = 1.0
lambda_TSVF = 0.01  # reduced coupling
v = 1.0
xi = 0.01  # weaker curvature coupling
n_steps = 2000

phi = np.random.normal(0, 0.1, (L, L))

def laplacian(f):
    return (
        -4 * f
        + np.roll(f, 1, axis=0)
        + np.roll(f, -1, axis=0)
        + np.roll(f, 1, axis=1)
        + np.roll(f, -1, axis=1)
    )

def scalar_curvature(phi):
    return laplacian(phi)

def action(phi):
    grad_sq = np.sum((np.roll(phi, 1, axis=0) - phi) ** 2)
    grad_sq += np.sum((np.roll(phi, 1, axis=1) - phi) ** 2)
    potential = lambda_TSVF * np.sum((phi**2 - v**2) ** 2)
    curvature_term = xi * np.sum(scalar_curvature(phi) * phi**2)
    return grad_sq + potential + curvature_term

def monte_carlo_step(phi, beta):
    for _ in range(L * L):
        i, j = np.random.randint(0, L, size=2)
        old_phi = phi[i, j]
        test_phi = old_phi + np.random.normal(0, 0.1)
        phi_trial = phi.copy()
        phi_trial[i, j] = test_phi
        dS = action(phi_trial) - action(phi)
        if dS < 0 or np.random.rand() < np.exp(-beta * dS):
            phi[i, j] = test_phi  # accept
    return phi

def enforce_retrocausal(phi):
    phi[-1, :] = np.conj(phi[0, :])
    return phi

actions = []
for step in range(n_steps):
    phi = monte_carlo_step(phi, beta)
    phi = enforce_retrocausal(phi)
    if step % 100 == 0:
        actions.append(action(phi))

# Plot results
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
