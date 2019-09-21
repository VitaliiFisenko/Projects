numbers=[1,2]
temp1 =0;
temp2 = 0;
while True:
	temp1 = numbers[0]+numbers[1]
	temp2 = numbers[1]
	numbers[0] = temp2
	numbers[1] = temp1
	print(numbers[1])
	if(numbers[1]>=4000000):
		break
