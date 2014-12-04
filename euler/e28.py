data = list(list(range(1001)) for i in xrange(1001))

data[500][500] = 1
begin,end = 499, 501 
cur = 2

while begin >= 0:
    for row in range(begin+1,end):
        data[row][end] = cur
        cur += 1
    for col in range(end, begin, -1):
        data[end][col] = cur
        cur += 1
    if begin < end:
        for row in range(end, begin, -1):
            data[row][begin] = cur
            cur += 1
        for col in range(begin, end+1):
            data[begin][col] = cur
            cur += 1
    begin -= 1
    end += 1

print sum(data[i][j] for i in range(1001) for j in range(1001) if i ==j or i+j == 1000)
