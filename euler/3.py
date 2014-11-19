import math

def isPrime(x):
	return all(x % p for p in xrange(2, x))

def findMaxPrimeFactor(x):
	f = x;
	while(f > 1):
		print f
		if(x % f == 0 and isPrime(f)):
			return f
		f = f - 1
	return 1

def findMaxPrimeFactor2(x):
	f = 2
	maxF = 1
	while(f <= x):
		if(isPrime(f)):
			print x, f
			while(x % f == 0):
				maxF = f
				x /= f
				print x
		f += 1
	print "maxF = %d" % maxF
	return maxF

	
print isPrime(10)
print isPrime(7)
print findMaxPrimeFactor2(600851475143)
	
