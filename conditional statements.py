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
#weather check
t = int(input("Enter temperature: "))
if t < 20:
  print("cold")
  if 20 <= t <= 30:
    print("pleasant")
    if t > 30:
      print("hot")


