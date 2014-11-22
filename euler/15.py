history = {}

def route(n,m):
	if n==0 or m==0:
		return 1
	elif history.has_key((n,m)):
		return history[(n,m)]
	else:
		history[(n,m)] = route(n-1,m)+route(n,m-1)
		return history[(n,m)]
	
print route(20,20)