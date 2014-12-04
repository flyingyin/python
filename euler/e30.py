def digitSum(n,p):
    return sum((int)(d) ** p for d in str(n))

print sum(n for n in xrange(2,  10 ** 6) if digitSum(n,5) == n)


