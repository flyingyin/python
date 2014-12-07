def isPandigital(n, m):
    digits = str(n) + str(m) + str(n*m)
    return reduce(lambda x,y:x+y, sorted(digits), '') == '123456789'

result = set(n*m for n in range(1, 9877) for m in range(n, 10000/n) \
 if isPandigital(n, m))

print result
print sum(result)
