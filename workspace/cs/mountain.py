def mountain(steps, l) :
	f = []
	if steps == 0:
		f.append(l.pop(0))
		f.append(l.pop(0))
		return f
	if steps == 1:
		first = l.pop(0)
		second = l.pop(0)
		middle = ((first[0] + second[0])/2, (first[1] + second[1])/2)
		f.append([first, middle, second])
		return f
	if steps >= 2:
		print "I dont know\n"
		return []

print mountain(1, [(10,10), (20,20)])

