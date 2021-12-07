from collections import Counter


with open('day6.txt', 'r') as fp:
    lanternfish = [int(x) for x in fp.readline().split(",")]
fish_dict = dict(Counter(lanternfish))

for i in range(0,9):
	try:
		print(fish_dict[i])
	except:
		fish_dict[i] = 0

print(fish_dict)

for i in range(1,257):
	new = fish_dict[0]
	for f in range(0,8):
		fish_dict[f] = fish_dict[f+1]
	fish_dict[8] = new
	fish_dict[6] += new
	print(f"Day {i}: {[(x, fish_dict[x]) for x in sorted(fish_dict)]}")

print(sum([fish_dict[x] for x in fish_dict]))
# lanternfish = [j]
# for i in range(1,256):
# 	for f in range(len(lanternfish)):
# 		lanternfish[f] -= 1
# 		#print(lanternfish[f])
# 		if lanternfish[f] == -1:
# 			lanternfish[f] = 6
# 			lanternfish.append(8)
# 	print(f"Day {i}")
# numbers[j] = len(lanternfish)
# print(numbers)