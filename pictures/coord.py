from random import randint
import numpy as np

coord = np.empty((0, 2))


for i in range(150):
	xy = np.array([[randint(0, 100), randint(0, 100)]])
	coord = np.append(coord, xy, axis=0)

np.save('coord.npy', coord)
