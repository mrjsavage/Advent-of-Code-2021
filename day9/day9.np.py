import numpy as np
from scipy import *

with open('day9.txt', 'r') as fp:
	grid = np.array([])
	i = 0
	j = 0
	for line in fp:
		if grid.size == 0:
			j = len(line) - 1
			grid = np.array(np.array([int(x) for x in list(line)[:-1]]))
		else:
			grid = np.append(grid, np.array([int(x) for x in list(line)[:-1]]))
		i+= 1
grid = grid.reshape((i, j))
print(grid)
print(np.gradient(grid,1))