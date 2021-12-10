pairs = {")":"(", "}":"{", ">":"<","]":"["}
scores = {")":3, "}":1197, ">":25137,"]":57}
closing_score = {"(":1, "[":2, "{":3,"<":4}
opens = list(pairs.values())

score_list = []
with open('day10.txt', 'r') as fp:
	score = 0
	for line in fp:
		liney = line[:-1]
		stack = []
		fine = True
		for l in liney:

			if l in opens:
				stack.append(l)
			else:
				if pairs[l] != stack.pop():
					fine = False
					score += scores[l]
					break
		if fine == True:
			cscore = 0
			while len(stack):
				cscore *= 5
				cscore += closing_score[stack.pop()]

			score_list.append(cscore)

print(score)
n = int((len(score_list) + 1)/2)
print(n)
s = sorted(score_list)
print(s[n - 1])
					