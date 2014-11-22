numbers = {0:'',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven'
           ,8:'eight',9:'nine',10:'ten',11:'eleven',12:'twelve',13:'thirteen'
           ,14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen'
           ,19:'nineteen',20:'twenty',30:'thirty',40:'forty',50:'fifty'
           ,60:'sixty',70:'seventy',80:'eighty',90:'ninety', 100:'hundred', 1000:'thousand'}

def charCnt(n):
	if n == 1000:
		return len(numbers[1]) + len('thousand')
	elif n >= 100:
		if n % 100 == 0:
			return len(numbers[n/100]) + len('hundred')
		elif n % 100 >= 20:
			return len(numbers[n / 100]) + len('hundredand') + len(numbers[(n % 100) / 10 * 10]) + len(numbers[n % 10])
		else:
			return len(numbers[n / 100]) + len('hundredand') + len(numbers[n % 100])
	elif n > 20:
		return len(numbers[n / 10 * 10]) + len(numbers[n % 10])
	else:
		return len(numbers[n])
		
print charCnt(300)
print sum((charCnt(n) for n in range(1, 1001)))