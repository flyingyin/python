def Fibonacci():
	x,y = 1,1
	while 1:
		yield x
		x,y = y,x+y

for i,v in enumerate(Fibonacci()):
	if len(str(v)) == 1000:
		print i
		break
	