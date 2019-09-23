def is_prime(a):
    return all(a % i for i in xrange(2, a))

def main_problem(n):
	a = 0
	i = 1
	while i<n:
		if n%i == 0 and is_prime(i):
			a = i	
			yield a
		i+=1
	

for x in main_problem(600851475143):
	print(x)