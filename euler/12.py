import math

primeList = [2]

def isPrime(n):
	for i in range(2, int(math.sqrt(n) + 1)):
		if(n %i == 0):	return False
	return True

def getNextPrime(n):	
	while(True):
		if(isPrime(n+1)):	return n+1
		else:	n += 1
	return n+1

def factorCount(n):
	sqrt = math.sqrt(n)
	while(primeList[-1] < sqrt):
		primeList.append(getNextPrime(primeList[-1]))
	
	factorCount = []
	for f in primeList:
		count = 0
		remain = n
		while(remain % f == 0):
			count += 1
			remain /= f
		factorCount.append(count)
	
	return reduce(lambda x,y : x*y, (c+1 for c in factorCount), 1)

def getTriangle(n):
	cur = 1
	triangle = 1
	while(factorCount(triangle) < n):
		cur += 1
		triangle += cur
	
	return triangle

print getTriangle(500)