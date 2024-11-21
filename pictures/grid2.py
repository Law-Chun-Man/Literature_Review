import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches

centre_x = 51
centre_y = 56
smoothing_radius = 20

def inside(xi, yi):
	distance = (centre_x-xi)**2 + (centre_y-yi)**2
	if distance <= smoothing_radius**2:
		return 1
	else:
		return 0


coord = np.load('coord.npy')


fig, ax = plt.subplots()


circle = patches.Circle((centre_x, centre_y), radius=smoothing_radius, edgecolor='black', facecolor='red', lw=2, zorder=0)
ax.add_patch(circle)

for xy in coord:
	if inside(xy[0], xy[1]):
		ax.scatter(xy[0], xy[1], color=(0.2, 0.8, 1.0), zorder=5)
	elif 20<xy[0]<80 and 20<xy[1]<80:
		ax.scatter(xy[0], xy[1], color=(0, 1, 0), zorder=5)
	else:
		ax.scatter(xy[0], xy[1], color='gray')


for i in range(0, 101, 20):
	ax.plot([0, 100], [i, i], color=(0, 0, 0))
	ax.plot([i, i], [0, 100], color=(0, 0, 0))


bottom_left = (20, 40)
square_side = 20
square = patches.Rectangle(bottom_left, square_side, square_side, color=(0, 1, 0, 0.2))
ax.add_patch(square)
bottom_left = (40, 40)
square_side = 20
square = patches.Rectangle(bottom_left, square_side, square_side, color=(0, 1, 0, 0.2))
ax.add_patch(square)
bottom_left = (60, 40)
square_side = 20
square = patches.Rectangle(bottom_left, square_side, square_side, color=(0, 1, 0, 0.2))
ax.add_patch(square)
bottom_left = (20, 20)
square_side = 20
square = patches.Rectangle(bottom_left, square_side, square_side, color=(0, 1, 0, 0.2))
ax.add_patch(square)
bottom_left = (40, 20)
square_side = 20
square = patches.Rectangle(bottom_left, square_side, square_side, color=(0, 1, 0, 0.2))
ax.add_patch(square)
bottom_left = (60, 20)
square_side = 20
square = patches.Rectangle(bottom_left, square_side, square_side, color=(0, 1, 0, 0.2))
ax.add_patch(square)
bottom_left = (20, 60)
square_side = 20
square = patches.Rectangle(bottom_left, square_side, square_side, color=(0, 1, 0, 0.2))
ax.add_patch(square)
bottom_left = (40, 60)
square_side = 20
square = patches.Rectangle(bottom_left, square_side, square_side, color=(0, 1, 0, 0.2))
ax.add_patch(square)
bottom_left = (60, 60)
square_side = 20
square = patches.Rectangle(bottom_left, square_side, square_side, color=(0, 1, 0, 0.2))
ax.add_patch(square)



ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.axis("off")
ax.set_aspect("equal")
ax.text(7, 21, "h", fontsize=20)

plt.savefig("grid2.png", bbox_inches="tight", pad_inches=0, transparent=True, dpi=600)
plt.show()
