def divisible(x, n):
	return all(( not x%p for p in range(1, n+1)))

def isPrime(x):
	return all(x % p for p in xrange(2, x))
	
def prodPrime(n):
	return reduce(lambda x,y: x * y, (x for x in range(1, n+1) if isPrime(x)), 1)

def minDivisible(n):
	prod = prodPrime(n)
	cur = prod
	while(1):
		print cur
		if(divisible(cur, n)): return cur
		cur += prod

print minDivisible(20)
