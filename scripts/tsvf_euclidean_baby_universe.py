
import numpy as np
import matplotlib.pyplot as plt

# Parameters
L = 16
beta = 1.0
lambda_TSVF = 0.01
v = 1.0
xi = 0.01
n_steps = 2000
delete_prob = 0.01  # probability of removing spacetime points (baby universes)

# Fields
phi = np.random.normal(0, 0.1, (L, L))
R = np.random.normal(0, 0.01, (L, L))
mask = np.ones((L, L), dtype=bool)  # true means active spacetime

def action(phi, R, mask):
    grad_x = (np.roll(phi, 1, axis=0) - phi) ** 2
    grad_y = (np.roll(phi, 1, axis=1) - phi) ** 2
    grad_sq = grad_x + grad_y
    potential = lambda_TSVF * (phi**2 - v**2) ** 2
    curvature_term = xi * R * phi**2
    total = grad_sq + potential + curvature_term
    return np.sum(total[mask])  # only over active spacetime

def monte_carlo_step(phi, R, mask, beta):
    for _ in range(L * L):
        # Update phi
        i, j = np.random.randint(0, L, size=2)
        if not mask[i, j]:
            continue
        old_phi = phi[i, j]
        new_phi = old_phi + np.random.normal(0, 0.1)
        phi_trial = phi.copy()
        phi_trial[i, j] = new_phi
        dS_phi = action(phi_trial, R, mask) - action(phi, R, mask)
        if dS_phi < 0 or np.random.rand() < np.exp(-beta * dS_phi):
            phi[i, j] = new_phi

        # Update R
        old_R = R[i, j]
        new_R = old_R + np.random.normal(0, 0.01)
        R_trial = R.copy()
        R_trial[i, j] = new_R
        dS_R = action(phi, R_trial, mask) - action(phi, R, mask)
        if dS_R < 0 or np.random.rand() < np.exp(-beta * dS_R):
            R[i, j] = new_R

    return phi, R

def enforce_retrocausal(phi, R, mask):
    phi[-1, :] = np.conj(phi[0, :])
    R[-1, :] = R[0, :]
    mask[-1, :] = mask[0, :]
    return phi, R, mask

def spawn_baby_universes(mask, prob=0.01):
    deletions = np.random.rand(*mask.shape) < prob
    mask[deletions] = False
    return mask

actions = []
for step in range(n_steps):
    mask = spawn_baby_universes(mask, delete_prob)
    phi, R = monte_carlo_step(phi, R, mask, beta)
    phi, R, mask = enforce_retrocausal(phi, R, mask)
    if step % 100 == 0:
        actions.append(action(phi, R, mask))

# Plot results
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
phi_vis = np.real(phi.copy())
phi_vis[~mask] = np.nan  # mask deleted regions
plt.imshow(phi_vis, cmap='plasma', origin='lower')
plt.colorbar(label='Field Value')
plt.title('Field Config (Re[ϕ]) with Baby Universes')

plt.subplot(1, 2, 2)
plt.plot(actions)
plt.title('Action over Monte Carlo Steps')
plt.xlabel('Step (x100)')
plt.ylabel('Action S_E')

plt.tight_layout()
plt.show()
