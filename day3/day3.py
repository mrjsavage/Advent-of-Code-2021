n = 0
count = [0]*12
ogen = []
co2 = []
with open('day3.txt', 'r') as fp:
	for line in fp:
		ogen.append(line)
		co2.append(line)
		for i, c in enumerate(line):
			if c == "1":
				count[i] += 1
			n += 1
c = count[0]
for i in range(0,9):
	if len(ogen) == 1:
		break
	else:
		if c >= n/2:
			ogen_iterator = filter(lambda x: (x[i] == "1"), ogen)
			ogen = list(ogen_iterator)
		else:
			ogen_iterator = filter(lambda x: (x[i] == "0"), ogen)
			ogen = list(ogen_iterator)

		c = 0
		for o in ogen:
			if o[i+1] == "1":
				c += 1
			n += 1


print(ogen)
# gamma = "".join(["1" if x > 500 else "0" for x in count])

# epsilon = "".join(["1" if x < 500 else "0" for x in count])

# print(gamma)
# print(epsilon)
# print(int(gamma,2) * int(epsilon, 2))