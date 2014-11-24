def getFactors(n):
	return [f for f in range(1, n) if n%f == 0]
	
def isAmicable(n):
	sumFactor = sum(getFactors(n))
	return n == sum(getFactors(sumFactor)) and n != sumFactor

print sum((n for n in range(1, 10000) if isAmicable(n)))