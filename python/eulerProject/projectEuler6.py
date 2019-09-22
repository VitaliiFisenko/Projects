#!Задача Эйлера 6
finalNumber =0 
num = [0,0]
ran = int(input())
for i in range(1,ran+1):
	finalNumber+=i**2
num[0] = finalNumber
print("сумма квадратов = "+str(finalNumber))
finalNumber = 0
for i in range(1,ran+1):
	finalNumber+=i
num[1] = finalNumber**2
print("Квадрат суммы = "+str(num[1]))
print("Разность квадрата суммы и суммы квадратов = "+str(num[1]-num[0]))
	