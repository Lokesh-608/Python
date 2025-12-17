#concatination
First_name="Malla"
Last_name="Reddy"
name=First_name+Last_name
print(name)
#reverse the string computer
s = "computer"
r=s[::-1]
print(r)
#operations
#add
a=10
b=20
c=a+b
print(c)
#sub
a=10
b=20
c=b-a
print(c)
#mult
a=10
b=20
c=b*a
print(c)
#division
a=10
b=20
c=b%a
print(c)
#Display 1 to 100 using loops
for i in range(1,101):
    print(i,end="")
#generate multiplication table
for i in range(1,10):
    s=+5*i
    print("5 X",i,"=",s)
#max,min
a=[10,20]
print(max(a))
print(min(a))
#123
# 23
#  3
n = 3
for i in range(n):
    for j in range(i):
        print(" ", end="")
    for k in range(i+1, n+1):
        print(k, end="")
    print()
#1.⁠ ⁠Write a program to print ⁠ "Hello, World!" ⁠.
s="Hello, World!"
print(s)
#2.⁠ ⁠Write a program to print your name, age, and city on separate lines.
n="Lokesh"
a=20
c="Ganapavaram"
print(n)
print(a)
print(c)
#3.⁠ ⁠Write a program that prints a multi-line string using triple quotes.
print("""Hello
Welcome to Python
This is a multi-line string""")
# 4.⁠ ⁠Write a program to take your name as input and print ⁠ "Hello, <name>!" ⁠.
s=str(input("Enter the name: "))
print("Hello",s)
#5.⁠ ⁠Write a program that asks the user for two numbers and prints their sum.
a=int(input("Enter the number: "))
b=int(input("Enter the number: "))
s=a+b
print(s)
#6.⁠ ⁠Write a program that asks the user for their age and prints whether they are a minor or an adult (just print the message, no conditions yet).
a=int(input("Enter the age: "))
if a>=18:
    print("An Adult")
else:
    print("A Minor")