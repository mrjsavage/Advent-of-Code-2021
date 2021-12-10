import numpy as np


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

low_points = []
for iy, ix in np.ndindex(grid.shape):
	a = grid[iy,ix]
	neighbours = []
	if iy < i - 1:
		neighbours.append(grid[iy + 1,ix])
	if iy >= 1:
		neighbours.append(grid[iy - 1,ix])
	if ix < j - 1:
		neighbours.append(grid[iy,ix + 1])
	if ix >= 1:
		neighbours.append(grid[iy,ix - 1])

	mimima = True
	for n in neighbours:
		if a >= n:
			mimima = False
	if mimima == True:
		print(f"({iy}, {ix}) {grid[iy,ix]}:", neighbours)
		low_points.append((a, iy, ix))

def basin_measure(grid, y,x,d=5):
	
	a = grid[y,x]
	if a == -1:
		return 0
	grid[y,x] = -1
	count = 1 if a != 9 else 0
	if y < i - 1:
		if grid[y + 1,x] >= a  and d != 1:
			count += basin_measure(grid, y + 1,x,0)
	if y >= 1:
		if grid[y - 1,x] >= a and d != 0:
			count += basin_measure(grid, y - 1,x,1)
	if x < j - 1:
		if grid[y,x + 1] >= a and d != 3:
			count += basin_measure(grid, y, x+1,2)
	if x >= 1 :
		if grid[y,x - 1] >= a and d != 2:
			count += basin_measure(grid, y, x-1,3)
	#print(f"({y},{x}) - {a}: Count {count}")

	return count
basin_size = []
for l in low_points:
	basin_size.append(basin_measure(grid, l[1], l[2]))
	if basin_size[-1] > 100:
		print(l, basin_size[-1])
print(sorted(basin_size))
print(basin_size[-3] * basin_size[-2]* basin_size[-1])
