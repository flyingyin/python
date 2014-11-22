def nextCollatz(n):
	if(n == 1):
		return 1
	return n/2 if n%2 == 0 else 3*n + 1

history = {}

def getCollatzSeqLen(n):
	if(n==1):	return 1
	elif(history.has_key(n)):	return history[n]
	else:	
		len = getCollatzSeqLen(nextCollatz(n)) + 1
		history[n] = len
		return len

maxLen = 1
result = 1
for n in range(1, 1000000):
	curLen = getCollatzSeqLen(n)
	if(curLen > maxLen):
		maxLen = curLen
		result = n
print result