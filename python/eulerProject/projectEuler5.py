number=0
i=0 
ran = int(input())
being= True
while being:
	i+=10
	for b in range(1,ran+1):
		if(i%b==0):			
			if(b==ran):
				being = False
		else:
			break
	print(i)
print(str(i))