from sympy.ntheory import divisors

def isAbundant(n):
	return sum(divisors(n)) > 2*n

def getAbundantSum(n):
	nums = [i for i in range(1,n+1) if isAbundant(i)]
	return set(a+b for a in nums for b in nums)
	
print sum(set(range(28124)).difference(getAbundantSum(28124)))