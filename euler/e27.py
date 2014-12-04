import math, itertools

def isPrime(n):
    if n < 2: return False
    for i in range(2, (int)(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def getProduct(a, b):
    return reduce(lambda x, y: x * y, itertools.takewhile(lambda n : isPrime(n ** 2 + a * n + b), xrange(1, abs(b))) , 1)

a,b = max(((a, b) for a in xrange(-999, 1000) for b in xrange(-999, 1000)), key = lambda (a,b): getProduct(a,b))

print a,b,a*b
