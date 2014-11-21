import time
import math

def isPrime(n):
  for p in range(2, int(math.sqrt(n))+1):
    if(n % p == 0): return False
  return True

s = time.time()
print reduce(lambda x,y : x + y, (p for p in xrange(2, 2000000) if isPrime(p)), 0)
e = time.time()

print e-s