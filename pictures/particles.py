import matplotlib.pyplot as plt
import numpy as np
coord = np.load('coord.npy')
coord = np.transpose(coord)


plt.scatter(coord[0], coord[1], color=(0.2, 0.8, 1.0))


plt.xlim(0, 100)
plt.ylim(0, 100)
plt.axis("off")
plt.gca().set_aspect("equal")

plt.savefig("particles.png", bbox_inches="tight", pad_inches=0, transparent=True, dpi=600)
plt.show()
