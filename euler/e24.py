def nextPermutation(l):
	for i in range(-2, -1 * len(l) - 1, -1):
		if l[i] > l[i+1]:  continue
		
		for j in range(-1, i, -1):
			if l[j] < l[i]:  continue
			l[i],l[j] = l[j],l[i]
			break
	
		tmp = l[i+1:]
		tmp.sort()
		l[i+1:] = tmp
		break
		
l = [i for i in '0123456789']
for i in range(999999):
	#print l
	nextPermutation(l)
print ''.join(l)
 