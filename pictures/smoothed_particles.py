import numpy as np
import matplotlib.pyplot as plt
coord = np.load('coord.npy')

def add_circular_gradient(ax, center=(0, 0), radius=1, color=(0.2, 0.8, 1.0), size=500):
    x = np.linspace(center[0] - radius, center[0] + radius, size)
    y = np.linspace(center[1] - radius, center[1] + radius, size)
    X, Y = np.meshgrid(x, y)

    Z = np.sqrt((X - center[0])**2 + (Y - center[1])**2)

    alpha = np.clip(1 - (Z / radius), 0, 1)

    rgba_image = np.zeros((size, size, 4))
    rgba_image[..., 0] = color[0]
    rgba_image[..., 1] = color[1]
    rgba_image[..., 2] = color[2]
    rgba_image[..., 3] = alpha

    ax.imshow(rgba_image, extent=(center[0] - radius, center[0] + radius, center[1] - radius, center[1] + radius), interpolation='bilinear')




fig, ax = plt.subplots()

for xy in coord:
    add_circular_gradient(ax, center=(xy[0], xy[1]), radius=5)

ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.axis('off')
ax.set_aspect("equal")

plt.savefig("smoothed_particles_5.png", bbox_inches="tight", pad_inches=0, transparent=True, dpi=600)
plt.show()
