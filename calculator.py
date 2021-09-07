num1 = eval(input("Enter the number: "))
num2 = eval(input("Enter 2nd the number: "))

cal = input("Choose one(add,subtract,divide,multiply):")
num3=0
if cal=="add":
	num3 = num1 + num2
elif cal=="subtract":
	num3 = num1 - num2
elif cal=="divide":
	num3 = num1 / num2
elif cal=="multiply":
	num3 = num1 * num2
else:
	print("Invalid Choice")

print("You Chose", cal)
print("Your result is",num3)