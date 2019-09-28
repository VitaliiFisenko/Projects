def fibon():
	a = b = 1 
	answer = 0
	while True:
		pass
		a,b =b,a+b
		if a%2 and a<=4000000:
			answer+=a
			yield answer
		elif a>4000000:
			yield answer
			break
for x in fibon():
	print(x)