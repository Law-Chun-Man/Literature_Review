import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.size'] = 30

fig, ax = plt.subplots()

h = 1
x = np.linspace(0, h, 500)
y = (h-x)**3

ax.plot(x, y, color='k')
ax.plot([1, 2], [0, 0], color='k')

ax.set_xlim(0, 1.5)
ax.set_ylim(-0.002, 1.1)
ax.set_aspect("equal")
ax.set_xlabel('r')
ax.set_ylabel('W')

ax.set_xticks([1])
ax.set_yticks([0, 1])
ax.set_xticklabels(['h'])
ax.set_yticklabels(['0', r'$h^3$'])
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)


plt.savefig("smoothing_kernel_2.png", bbox_inches="tight", pad_inches=0, transparent=True, dpi=600)
plt.show()
