import numpy as np


def flash(grid, iy, ix):
	for i in range(-1,2):
		for j in range(-1,2):
			if j == 0 and i == 0:
				pass
			else:
				if abs(4.5 - ix - i) > 4.5 or abs(4.5 - iy - j) > 4.5:
					print(f"{ix + i}, {iy + j}")
				else:
					grid[iy+j,ix+i] += 1
					if grid[iy+j,ix + i] >= 10:
						grid[iy+j,ix + i] = -1000
						grid = flash(grid,iy+j,ix+i)

	return grid

with open('day11.txt', 'r') as fp:
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
tots = 0
s = 0
while True:
	s += 1 
	grid = grid + 1
	for y in range(0,10):
		for x in range(0,10):
			if grid[y,x] == 10:
				grid[y,x] = -1000
				print(grid)
				grid = flash(grid,y,x)

	result = np.where(grid < 0)
	listOfCoordinates= list(zip(result[0], result[1]))

	tflash = len(listOfCoordinates)
	for cord in listOfCoordinates:
		grid[cord[0],cord[1]] = 0

	print(f"After step {s} - {tflash}")
	#print(grid)
	tots += tflash
	if tflash == 100:
		break

print(tots)