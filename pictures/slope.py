import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.size'] = 30

fig, ax = plt.subplots()

h = 1
x = np.linspace(0, 1, 500)
y = (h**2-x**2)**3

def dydx(x, h):
    return -6 * x * (h**2 - x**2)**2

x_tangent = 0.06
y_tangent = (h**2 - x_tangent**2)**3
slope_tangent = dydx(x_tangent, h)
tangent_line = slope_tangent * (x - x_tangent) + y_tangent
ax.plot(x, tangent_line, '--r', label=f'Tangent at x = {x_tangent}')

ax.plot(x, y, color='k')
ax.plot([1, 2], [0, 0], color='k')

ax.set_xlim(0, 1.5)
ax.set_ylim(-0.001, 1.1)
ax.set_aspect("equal")
ax.set_xlabel('r')
ax.set_ylabel('W')

ax.set_xticks([1])
ax.set_yticks([0, 1])
ax.set_xticklabels(['h'])
ax.set_yticklabels(['0', r'$h^6$'])
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.savefig("slope.png", bbox_inches="tight", pad_inches=0, transparent=True, dpi=600)
plt.show()
