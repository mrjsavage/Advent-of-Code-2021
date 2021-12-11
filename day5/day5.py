import re
import numpy as np

grid = np.zeros((2, 1000, 1000))
ls = np.fromregex(open('day5.txt', 'r'), '\d+', [('',int)]*4)
for (x, y, X, Y) in ls:
    dx, dy = np.sign([X-x, Y-y])                 
    while (x,y) != (X+dx, Y+dy):
        grid[dx * dy, x, y] += 1
        x+=dx; y+=dy

print((grid[0]>1).sum(), (grid.sum(0)>1).sum())

# with open('day5.txt', 'r') as fp:
# 	for line in fp:
# 		m = re.match("([0-9]*),([0-9]*) -> ([0-9]*),([0-9]*)", line)
# 		if (m.group(1) == m.group(3)):
# 			x = int(m.group(1))
# 			start = int(min(m.group(2), m.group(4)))
# 			end = int(max(m.group(2), m.group(4))) + 1
# 			for y in range(start,end):
# 				vents[x,y] += 1
# 		elif (m.group(2) == m.group(4)):
# 			y = int(m.group(2))
# 			start = int(min(m.group(1), m.group(3)))
# 			end = int(max(m.group(1), m.group(3))) + 1
# 			for x in range(start,end):
# 				vents[x,y] += 1

# print(vents > 1)
# print(np.count_nonzero(vents > 1))
			
