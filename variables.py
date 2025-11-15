# Casting variables converting float into integer
d = 10.23
s = int(d)
print(s)

# Given an input num as a string. You need to typecast into an integer and double it. 
num = "5"
s = int(num)
i = num*2
print(type(i))

# swap two numbers
a = 1
b = 2
a,b = b,a
print(a,b)

# Area of a triangle
l = 4
b = 6
a = l*b
print("Area of triangle: ",a)

#simple interest
a = input("Enter principal: ")
b = input("Enter rate: ")
c = input("Enter time: ")
p = int(a)
r = int(b)
t = int(c)
SI = (p * r * t)/100
print("Simple Interest: ",SI)

#Temperature conversion
a = input("Enter celsius: ")
C = int(a)
F = (C * 9/5) + 32
print("Fahrenheit: ",F)

#Perimeter of a square
i = input("Enter side of square: ")
a = int(i)
P = 4*a
print("Perimeter of a square: ",P)

#Average of three numbers
a,b,c = 10,20,30
sum = a+b+c
print(sum)

# Area of a circle
r = int(2)
a = 3.14 * r * r
print("Area of circle: ",a)

Convert Hours to minutes
x = input("Enter hour: ")
