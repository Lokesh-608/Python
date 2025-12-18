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
#7.⁠ ⁠Write a program that uses ⁠ input() ⁠ to read a string and then prints its length.
s=str(input("Enter the String: "))
print(len(s))
#8.⁠ ⁠Write a program to read a line from the user and print it in this format:
  # ⁠ You entered: <user_input> ⁠.
s=input("Enter the String: ")
print("You entered: ",s)
#9.⁠ ⁠Write a program that reads your full name and prints it in one line and then in two lines (first name on first line, last name on second).
full_name=input("Enter the name: ")
print(full_name)
f_name,l_name=full_name.split()
print(f_name)
print(l_name)
#11.⁠ ⁠Write a program that asks the user for three values and prints them using an f-string in one sentence.
a=input("Enter the String: ")
b=input("Enter the String: ")
c=input("Enter the String: ")
print(f" {a},{b},{c}")
#10.⁠ ⁠Write a program that takes two numbers as strings from the user and shows the difference between string concatenation and numeric addition.
a=int(input("Enter the number: "))
b=int(input("Enter the number: "))
c=str(a)
d=str(b)
w=c+d
s=a+b
print(w)
print(s)
#12.⁠ ⁠Write a program that demonstrates the use of ⁠ sep ⁠ and ⁠ end ⁠ parameters in ⁠ print() ⁠.
a="String"
c="method"
print(a,c,sep="-")
b="Hello"
d="world"
print(b,end=" ")
print(d)
#13.⁠ ⁠Write a program that prints a formatted table-like output using ⁠ \t ⁠ and ⁠ \n ⁠.

print("Name\tAge\tBranch")
print("Lokesh\t20\tcse")
print("Ashri\t20\tcse")
#14.⁠ ⁠Write a program that reads a float from the user and prints it rounded to 2 decimal places.
num = float(input("Enter a number: "))
print(round(num, 2))
#15.⁠ ⁠Write a program that shows the difference between ⁠ print(5) ⁠ and ⁠ print("5") ⁠.
s=5
print(s)
#it prints the s only
print("s")

## B. Variables (16–25)

#16.⁠ ⁠Write a program that stores your name, age, and CGPA in variables and prints them.
s="Lokesh"
t="20"
y="8.8"
print(s)
print(t)
print(y)
#17.⁠ ⁠Write a program to swap two variables using a temporary variable.
a="CSE"
b="DS"
a,b=b,a
c=a,b
print(c)
#18.⁠ ⁠Write a program to swap two variables *without* using a temporary variable.
a="CSE"
b="DS"
a,b=b,a
print(a,b)
#19.⁠ ⁠Write a program that assigns the same value to three variables in one line and prints them.
a=b=c=10
d=a,b,c
print(d)
#20.⁠ ⁠Write a program that demonstrates multiple assignment like ⁠ a, b, c = 1, 2, 3 ⁠.
a,b,c=10,10,10
d=a,b,c
print(d)