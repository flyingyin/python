coins = (1,2,5,10,20,50,100,200)
sol = list(list(0 for _ in xrange(201)) for _ in range(len(coins)+1))
sol[0][0] = 1

for num in range(1, len(coins)+1):
    for count in range(201):
        for c in range(count / coins[num-1]+1):
          sol[num][count] += sol[num-1][count - c * coins[num-1]]

print sol[-1][-1]

