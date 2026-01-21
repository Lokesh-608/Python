#Check whether a number is Prime
num = int(input("Enter a number: "))

if num <= 1:
    print("It is not prime")
else:
    for i in range(2, num):
        if num % i == 0:
            print("It is not prime")
            break
    else:
        print("It is prime")
#Check Palindrome Number
num =int(input("Enter the number: "))
n = str(num)
if n == n[::-1]:
    print("It is palindrome")
else:
    print("It is not palindrome")
    #Check Armstrong Number
num=int(input("Enter the numbe: "))
original = num
n=str(num)
count = len(n)
sum=0
for ch in n:
    digit=int(ch)
    total=digit**count
    sum+=total
    if sum==original:
        print("It is armstrong")
    else:
        print("It is not a armstrong")
#Print Fibonacci Series
n=int(input("Enter the numbe: "))
f=0
l=1
for i in range(n):
    print(f)
    next=f+l
    f=l
    l=next



