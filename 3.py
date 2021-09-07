num = eval(input("Enter the number"))

sum = 0
temp = num
while temp > 0:
	r = temp%10
	temp = temp//10
	sum = sum+r**3
if(sum==num):
	print("sum of digits are",sum)