def nameScore(name, pos):
	return sum((ord(c.lower()) - ord('a') + 1 for c in name[1:-1])) * pos

names = open('p022_names.txt').readline().split(',')
names.sort()

print sum(map(nameScore, names, xrange(len(names))))