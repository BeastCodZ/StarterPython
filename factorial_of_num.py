num = int(input("Enter the number:"))
fact = 1
if num<0:
	print("Negetive number dont have factorial")
elif num==0:
	print("Factorial of number zero is one")
else:
	i = num
	while i>=1:
		fact = fact*i
		i = i-1

	print("The factorial of",num,"is",fact)
