#to check if a number is prime or not
import math

num = int(input("Enter the number:"))
flag = 0
if num>1:
	for i in range(2,int(math.sqrt(num))+1):
		if num%i==0:
			flag = 1
		break
if flag == 0:
	print(num,"is a prime number.")
else:
	print(num,"is not a prime number.")