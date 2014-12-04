import random
import matplotlib.pyplot as plt

pos = [i for i in range(20 + 2*8)]
freq = {}
cur = 0

for key in range(len(pos)):
  freq[key] = 0 

for iter in range(1000000):
  x = random.randint(1,6)
  y = random.randint(1,6)
  cur += x + y
  cur %= len(pos)
  freq[cur] += 1

print freq.values()

plt.figure(1)
print plt.bar(freq.keys(), freq.values())
plt.show()
  

