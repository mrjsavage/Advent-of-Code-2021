import numpy as np
import re



coords = []
folds = []
incoords = True
prog = re.compile(r"fold along ([xy])=(\d*)\n")
with open('day13.txt', 'r') as fp:
	for line in fp:
		if len(line.strip()) == 0:
			incoords = False
		elif incoords == True:
			coords.append([int(x) for x in line.strip().split(',')])
		else:
			m = prog.match(line)
			folds.append([m[1],int(m[2])]) 

height = max([x[1] for x in coords])
width = max([x[0] for x in coords])



paper = np.zeros(shape=(height + 1,width+1), dtype=int)


for x, y in coords:
	paper[y,x] = 1
#print(height,width)
axis, index =  folds[0]
ax = 1 if axis == "x" else 0
nax = 1 ^ 1
print(ax, nax)
folded = np.array_split(paper, [index,index+1], axis=ax)
folded[2] = np.flip(folded[2],axis=ax)
a = abs(folded[0].shape[ax] - folded[2].shape[ax])
b = folded[0].shape[nax]

h = (ax * a) + (nax * b)
w = (ax * b) + (nax * a)
print(h,w)
if folded[2].shape[ax] > folded[0].shape[ax]:
	h = folded[2].shape[ax] - folded[0].shape[ax]
	w = folded[2].shape[ax] - folded[0].shape[ax]
	print(h,w)
	tmp  = np.zeros(shape=(w+1,h+1), dtype=int)
	print(tmp.shape, folded[0].shape)
	folded[0] = np.concatenate([tmp,folded[0]])
elif folded[2].shape[ax] < folded[0].shape[ax]:
	h = folded[2].shape[ax] - folded[0].shape[ax]
	w = folded[2].shape[ax] - folded[0].shape[ax]
	print(h,w)
	tmp  = np.zeros(shape=(w+1,h+1), dtype=int)
	print(tmp.shape, folded[0].shape)
	folded[0] = np.concatenate([tmp,folded[0]])
else:
	pass
print(folded[0].shape)
	#print(folded[1].shape)
	#paper = 1*np.logical_or(folded[0],folded[2],dtype=int)
	#print(np.sum(paper))
print(paper)