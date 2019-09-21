inp = int(input())
def checkForTrue(variable):
	check = True
	for n in range(2,variable):
		if variable%n!=0:
			chek = True
		else:
			check = False
	return check
for i in range(1,inp+1):
	if(inp%i==0):
		if checkForTrue(i):
			print(i)
		else:
			continue

