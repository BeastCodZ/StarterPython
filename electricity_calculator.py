#A program to calculate average of 5 subjects

name = (input("Write your name: "))

units = eval(input("How many number of units you consumed: "))

if(units >= 500):
	amount = units * 9.65
	surcharge = 85
elif(units >= 300):
	amount = units * 7.75
	surcharge = 85
elif(units >= 200):
	amount = units * 5.26
	surcharge = 85
elif(units >= 100):
	amount = units * 3.76
	surcharge = 85
else:
	amount = units * 2.25
	surcharge = 25
total = amount + surcharge
print("\n",name,)
print("your Electicity Bill is %.2f" %total)
