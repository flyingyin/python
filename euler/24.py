def nextPermutation(l):
	for i in [len(l)-2:0:-1]:
		if l[i] > l[i+1]:  continue
		l[i-1],l[-1] = l[-1],l[i-1]
		tmp = l[i+1:]
		tmp.sort()
		l[i+1:] = tmp
 