import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import brentq

def f(x):
    return 1 + np.cosh(x) * np.cos(x)

# Plot range
xmin, xmax = -50, 50
x = np.linspace(xmin, xmax, 20001)   # dense grid so we don't miss sign flips
y = f(x)

# Find sign-change intervals
roots = []
for i in range(len(x) - 1):
    y1, y2 = y[i], y[i + 1]
    if np.isfinite(y1) and np.isfinite(y2):
        if y1 == 0:
            roots.append(x[i])
        elif y1 * y2 < 0:  # sign change -> bracketed root
            r = brentq(f, x[i], x[i + 1])
            # de-duplicate
            if not any(np.isclose(r, rr, atol=1e-6) for rr in roots):
                roots.append(r)

roots = sorted(roots)

# Print solutions
print("Roots in [-50, 50]:")
for r in roots:
    print(f"{r:.12f}")

# Plot
plt.figure()
plt.plot(x, y, c='orange')
plt.axhline(0, c='grey', linestyle='--')

# Blue balls at the zeros
plt.plot(roots, [0]*len(roots), 'bo')

plt.xlim([xmin, xmax])
plt.ylim([-100, 100])  # keeps it readable; adjust if you want

plt.savefig('coshcos.png', dpi=500)

plt.show()