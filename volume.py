#find value of cone 

name = input("Write your name: ")

radius = input("Enter Radius: ")

height = input("Enter height: ")

r = eval(radius)

h = eval(height)

vol = 1/3 * 22/7 * r**2 * h

print(name,",your volume is",vol)