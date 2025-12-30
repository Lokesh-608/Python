#if statement
a = 33
b = 200
if b > a:
  print("b is greater than a")
#even or odd
a = 30
if a%2==0:
 print("a is even")
else:
  print("a is not even")
 #positive or negative
a = 20
if a<0:
  print("a is negative ")
else:
  print("a is positive")
#eligibilty for vote
a = 18
if a>=18:
  print("a is eligible for voting")
else:
  print("a is not eligible for voting")
#check divisible
a = 5
if a%5==0:
  print("a is divisible of 5")
else:
  print("a is not divisible of 5")
  #elif
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
#and
a = 200
b = 33
c = 500
if a > b and c > a:
  print("both cases are true")
#or
a = 200
b = 33
c = 500
if a > b or c > a:
  print("atleast one condition iss true")
  #not
a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")
#nested if
x = 41
if x > 10:
  print("x is greater 10")
  if x > 20:
    print("x is greater then 10 and 20")
  else:
    print("x is not greater than 20")
#calculate
def calculate(a, b, operator):
    if operator == 1:
        print(a + b, end="")   
    elif operator == 2:
        print(a - b, end="")   
    elif operator == 3:
        print(a * b, end="")   
    else:
        print("Invalid Input", end="")  
        calculate(1, 2, 3) 
#marks condition
a = 50
if a >= 40:
 print("passed")
 if a >= 75:
   print("distinction")
#weather check nested if
t = int(input("Enter temperature: "))
if t < 20:
  print("cold")
  if 20 <= t <= 30:
    print("pleasant")
    if t > 30:
      print("hot")
#Leap Year
y = int(input("Enter year: "))
if y%400==0:
  print("It is leap year: ")
else:
  print("It is not leap year: ")
  #Grade Calculator
g = int(input("Enter marks: "))
if 90 < g < 100:
    print("A Grade")
elif 75 < g < 89:
    print("B Grade")
elif 50 < g < 74:
    print("C Grade")
elif g < 50:  
    print("Fail")
else:
    print("Invalid marks entered.") 
#check if number is even and also divisible by 4
i = int(input("Enter number: "))
if i%2==0:
   print("It is even")
   if i%4==0:
      print("It is also even")
   else:
      print("the number is not even")
#greatest of two numbers
i = int(input("Enter number: "))
s = int(input("Enter number: "))
if i>s:
   print("i is greater than s")
else:
   print("s is greater than i")
#adult or not
a=10
if a >=10:
   print("adult")
else:
   print("Not adult")
#check the number is even or odd
s = int(input("Enter the number: "))
if s%2==0:
   print("It is even")
elif s%3==0:
   print("It is odd")
else:
   print("It is zero")
