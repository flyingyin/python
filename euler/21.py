def getFactors(n):
	return (f for f in range(1, n+1) if n%f == 0)
	
def isAmicable(n):
	sumFactor = sum(getFactors(n))
	return sumFactor == getFactors(sumFactor)

print sum((n for n in range(1, 1001) if isAmicable(n)))