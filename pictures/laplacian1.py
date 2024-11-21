import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.size'] = 30

fig, ax = plt.subplots()

h = 1
x = np.linspace(0, h, 500)
y = -x**3/2/h**3+x**2/h**2+h/2/x-1
laplacian_y = (x**2*(h/x**3+2/h**2-3*x/h**3)+2*x*(-h/2/x**2+2*x/h**2-3*x**2/2/h**3))/x**2

ax.plot(x, y, color='k')
ax.plot(x, laplacian_y, '--r', label=r"$\nabla^2 W$")
ax.plot([1, 2], [0, 0], color='k')

ax.set_xlim(0, 1.5)
ax.set_ylim(0, 1.3)
ax.set_aspect("equal")
ax.set_xlabel('r')
ax.set_ylabel('W')


ax.set_xticks([1])
ax.set_yticks([0])
ax.set_xticklabels(['h'])
ax.set_yticklabels(['0'])
ax.spines['bottom'].set_position(('data', 0))
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.legend(fontsize=18)

plt.savefig("laplacian1.png", bbox_inches="tight", pad_inches=0, transparent=True, dpi=600)
plt.show()
