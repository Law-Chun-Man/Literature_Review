import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig, ax = plt.subplots()

particles = np.array([[34, 28],
					  [71, 25],
					  [25, 30],
					  [10, 42],
					  [3, 3],
					  [3, 56],
					  [65, 36],
					  [30, 22],
					  [22, 35],
					  [15, 47]])

for i in range(len(particles)):
	ax.scatter(particles[i][0], particles[i][1], c=(0.2, 0.8, 1))
	ax.text(particles[i][0]+1, particles[i][1]+1, str(i), fontsize=12, c='blue')

count = 0
for j in range(3):
	for i in range(4):
		x, y = i*20, j*20
		side_length = 20
		square = patches.Rectangle((x, y), side_length, side_length, lw=2, edgecolor='black', facecolor='none')
		ax.add_patch(square)
		label_x = x + side_length-1.5
		label_y = y + side_length-1.5
		ax.text(label_x, label_y, str(count), color='black', ha='right', va='top', fontsize=12)
		count += 1


ax.set_xlim(0, 80)
ax.set_ylim(0, 60)
ax.set_aspect('equal')
ax.axis("off")


plt.savefig("grid3.png", bbox_inches="tight", pad_inches=0, transparent=True, dpi=600)
plt.show()
