import queue

count = 0
q = queue.Queue()
with open('day1.txt', 'r') as fp:
	
	for line in fp:
		cur = int(line)
		q.put(cur)
		if q.qsize() == 4:
			out = q.get()
			tot = sum(list(q.queue))
		if last != None:
			if last < tot:
				count += 1
			last = tot
		elif q.qsize() == 3:
			last = tot
		print(last, tot, out, list(q.queue))
		
print(count)
