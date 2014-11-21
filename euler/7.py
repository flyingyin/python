import time
import math

def isPrime(n):
  for p in range(2, int(math.sqrt(n))+1):
    if(n % p == 0): return False
  return True
  
def isPrime2(n):
  return all((n % p for p in range(2, n)))

def getPrime(idx):
  cur = 0
  curIdx = 1
  while(curIdx <= idx):
    while(True):
      if(isPrime(cur)):
        #print(cur)
        cur += 2
        break
      cur += 1
    curIdx += 1
  return cur


s = time.time()
print(getPrime(10001))
e = time.time()
print(e - s)