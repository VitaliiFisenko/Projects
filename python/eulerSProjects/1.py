"""%3 == 0 && %5 == 0"""

"""def sum(n):
	a = 0;
	for i in range(n):
		
		if i%3 == 0 or i%5 == 0 :
			a+=i
			yield a

for x in sum(1000):
	print(x)
	"""
	
a = 0
for x in range(1000):
	if x%3 == 0 or x%5 == 0:
		a+=x
print(a)