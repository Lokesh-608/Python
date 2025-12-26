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
#21.⁠ ⁠Write a program that reads two numbers and stores their sum, difference, product, and quotient in four different variables and prints all.
a=int(input("Enter the value: "))
b=int(input("Enter the value: "))
s=a+b
c=a*b
f=a-b
g=a/b
print(s)
print(c)
print(f)
print(g)
#22.⁠ ⁠Write a program to show what happens if you reassign a variable from int to string.
x = 10
print(x)
x = "Hello"
print(x)
#23.⁠ ⁠Write a program that uses descriptive variable names for calculating the area of a rectangle.
length=int(input("enter the num: "))
breadth=int(input("enter the num: "))
area=length*breadth
print(area)
#24.⁠ ⁠Write a program that shows why using names like ⁠ list ⁠ or ⁠ str ⁠ as variable names is a bad idea.
list = [1, 2, 3]
print(list)

#by using built in function list it shows a error
x = list("abc")
print(x)
#25.⁠ ⁠Write a program that uses a constant-like variable (e.g. ⁠ PI = 3.14 ⁠) and calculates the area of a circle.

r=int(input("Enter the num: "))
Area=3.14*r*r
print(Area)

### C. Operators (26–45)
#⁠26.Write a program to add, subtract, multiply, and divide two numbers.
a=int(input("Enter the num: "))
b=int(input("Enter the num: "))
d=a+b
g=a-b
f=a*b
z=a%b
print(d,g,f,z)
#27.⁠ ⁠Write a program that uses the floor division (⁠ // ⁠) and modulus (⁠ % ⁠) operators and prints the results for two integers.
a=10
b=20
c=a//b
d=a%b
print(c,d)
#28.⁠ ⁠Write a program to calculate ⁠ a ⁠ raised to the power ⁠ b ⁠ using ⁠ ** ⁠.
a=10
b=2
d=a**b
print(d)
#29.⁠ ⁠Write a program that compares two numbers and prints which one is greater using comparison operators.
a=10
b=20
if a>b:
    print(a)
else:
    print(b)
#30.⁠ ⁠Write a program that checks if two given numbers are equal or not.
a=10
b=20
if a==b:
    print("Numbers are equal")
else:
    print("Not Equal")
#31.⁠ ⁠Write a program that demonstrates all comparison operators (⁠ ==, !=, >, <, >=, <= ⁠) with sample values.
a=10
b=20
if a==b:
    print("It is equal")
elif a!=b:
    print("It is not equal")
elif a>b:
    print("a is greater ")
elif a<b:
    print("b is gretaer")
elif a>=b:
    print("a s gretaer equal b")
elif a<+b:
    print("b is gretaer equa a")
else:
    print("no change")
#32.⁠ ⁠Write a program that uses logical operators (⁠ and ⁠, ⁠ or ⁠, ⁠ not ⁠) to check if a number is in the range 10 to 20.
#33.⁠ ⁠Write a program that checks if a given year is between 2000 and 2025 and not equal to 2010.
a = int(input("Enter a year: "))

if 2000 <= a <= 2025 and a != 2010:
    print("a is between 2000 and 2025 and not equal to 2010.")
else:
    print("It is not satisfy")
#34.⁠ ⁠Write a program to show the effect of operator precedence in an expression like ⁠ 3 + 4 * 2 ** 3 ⁠.
#36.⁠ ⁠Write a program to demonstrate assignment operators (⁠ += ⁠, ⁠ -= ⁠, ⁠ *= ⁠, ⁠ /= ⁠, ⁠ //= ⁠, ⁠ %= ⁠, ⁠ **= ⁠) on a variable.
a=10
print(a)
a+=4
print(a)
a-=5
print(a)
a*=2
print(a)
a/=3
print(a)
a//=4
print(a)
a%=6
print(a)
a**=3
print(a)
#37.⁠ ⁠Write a program to check if a number is even using the modulus operator.
a=int(input("Enter the number: "))
if a%2==0:
    print("It is even ")
else:
    print("It is not even")
#38.⁠ ⁠Write a program to check if a number is a multiple of both 3 and 5 using logical operators.
a=int(input("Enter the number: "))
if a%3==0 | a%5==0:
    print("It is multiple of 3 andd 5")
else:
    print("It is not multiples of 3 and 4")
#39
a=int(input("Enter the number: "))
if a%4==0 | a%3==0:
    print("It is multiple of 3 andd 5")
else:
    print("It is not multiples of 3 and 4")
#39.⁠ ⁠Write a program that reads three numbers and prints the largest using only comparison operators (no ⁠ max() ⁠).
a=int(input("Enter the num: "))
b=int(input("Enter the num: "))
c=int(input("Enter the num: "))
if a>b&a>c:
    print(a)
elif b>a&b>c:
    print(b)
elif c>a&c>b:
    print(c)
else:
    print("no numbers")
#40.⁠ ⁠Write a program to demonstrate the difference between ⁠ / ⁠ and ⁠ // ⁠ when dividing integers.
#/ it prints quoitent
a=10
b=20
c=a/b
print(c)
#// it prints remainder
a=10
b=20
c=a/b
print(c)
#41.⁠ ⁠Write a program that uses bitwise operators (⁠ & ⁠, ⁠ | ⁠, ⁠ ^ ⁠, ⁠ << ⁠, ⁠ >> ⁠) on two small integers and prints the results.
a=10
b=20
c=30
#&
if a>b&a>c:
    print("a is greater")
#|
a=10
b=20
c=30
if a>b|a>c:
    print("a is greater")
#^
a=10
b=20
c=a^b
print(c)
#<<
a=3
b=20
if a<<b:
    print("b is greater")
#>>
a=6
b=2
if a>>b:
    print("a is greater")
#42.⁠ ⁠Write a program that checks if a number is odd using a bitwise operation.
a=30
if a%3&a%9:
    print("it is odd")
#44.⁠ ⁠Write a program that demonstrates the use of ⁠ in ⁠ and ⁠ not in ⁠ operators on a string.
k=[1,2,3,4,5]
if 1 in k:
    print("1 is present in k")
else:
    print("1 is not present" )
#not in
r=[1,2,3,4]
if 5 not in r:
    print("5 is not present in r")
else:
    print("5 is present in r")
#79. Write a program to create a dictionary with keys: ⁠ name ⁠, ⁠ age ⁠, ⁠ city ⁠ and print it.
p = {
    "name": "Lokesh",
    "age": 21,
    "city": "Hyderabad"
}

print(p)
#181. Write a program that adds a new key–value pair to an existing dictionary.
# Existing dictionary
s = {
    "name": "Lokesh",
    "age": 21,
    "course": "CSE"
}

# Adding a new key-value pair
s["college"] = "Malla reddy university"

# Printing updated dictionary
print(s)
#46.⁠ ⁠Write a program that uses ⁠ if ⁠, ⁠ elif ⁠, and ⁠ else ⁠ to categorize a number as negative, zero, or positive.
a=int(input("Enter the number: "))
if a>=0:
    print("a is positive")
elif a<=0:
    print("a is negative")
else:
    print("a is zero")
## for loop example
print("Using for loop:")
for i in range(1, 6):
    print(i)
#while loop
# while loop example
print("Using while loop:")
i = 1
while i <= 5:
    print(i)
    i += 1
#48.⁠ ⁠Write a program that uses the ⁠ break ⁠ keyword to exit a loop when a certain condition is met.
i=1
while i<=5:
    break
i=3
print(i)
#Write a program that checks if a given year is a leap year.
a=2026
if a%100==0:
    print("It is leapyear")
#91.⁠ ⁠Write a program to print numbers from 1 to 10 using a ⁠ for ⁠ loop.
i=11
for i in range(1,i):
    print(i)
## Creating a set of integers
numbers = {1, 2, 3, 4, 5}
print(numbers)
#192. Write a program that adds an element to a set using ⁠ add() ⁠.
num = {1, 2, 3}
num.add(4)
print(num)
