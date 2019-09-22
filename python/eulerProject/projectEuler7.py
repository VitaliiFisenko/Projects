#! Программа для нахождения n-того простого числа

rn = int(input())
i = 1
n = 1

def checkForTrue(variable):
	check = True
	for n in range(2,variable):
		if variable%n!=0:
			chek=True
		else:
			check = False
	return check


while i<=rn:
	n+=1
	if checkForTrue(n):
		print(str(n) +" - это "+ str(i))
		i+=1
	else:
		continue