import re
from collections import Counter
template ={}

with open('day14.txt', 'r') as fp:
	polymer = fp.readline().strip()
	for line in fp:
		template[line[0:2]] = line[6]


counts = Counter([polymer[i:i+2] for i in range(len(polymer) -1 )])
print(counts)
for i in range(1,41):
	tmp = Counter()
	for t in counts:
		if t in template:
			tmp[f"{t[0]}{template[t]}"] += counts[t]
			tmp[f"{template[t]}{t[1]}"] += counts[t]
	counts = tmp.copy()
	if i in [10,40]:
		total = Counter()
		for c in counts:
			total[c[0]] += counts[c]
		total[polymer[-1]] += 1
		print(max(total.values()) - min(total.values()))

print(Counter(polymer))
print(sorted(list(Counter(polymer).values()))[-1] - sorted(list(Counter(polymer).values()))[0])