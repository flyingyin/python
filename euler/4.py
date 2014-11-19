import itertools

def isPalindrome(x):
	return str(x) == str(x)[::-1]
	
print max((p[0] * p[1] for p in itertools.combinations(range(100,1000), 2) if isPalindrome(p[0]*p[1])))