#A program to calculate average of 5 subjects

name = input("Write your name: ")

english = input("Enter the marks of english: ")

maths = input("Enter the marks of maths: ")

hindi = input("Enter the marks of hindi: ")

social_science = input("Enter the marks of social science: ")

science = input("Enter the marks of science: ")

e = eval(english)

m = eval(maths)

h = eval(hindi)

s = eval(social_science)

sc = eval(science)

av = (e+m+h+s+sc)/5

print("Average marks of ",name,"are ",av)