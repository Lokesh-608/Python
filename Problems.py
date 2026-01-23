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
num =str(input("Enter the number: "))

if num== num[::-1]:
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
#Reverse string
s=input("Enter the string: ")
rev=s[::-1]
print(rev)
#Second largest in array
a = input("Enter the numbers: ")
s = a.split()

n = []
for ch in s:
    n.append(int(ch))

large = n[0]
second = n[0]

for i in n:
    if i > large:
        second = large
        large = i
    elif i < large and i > second:
        second = i

print("Second largest number is:", second)
#Anagram check
a=str(input("Enter the name: "))
b=str(input("Enter the name: "))
c=len(a)
d=len(b)
if c==d:
    print("It is anagram")
else:
    print("It is not anagram")
#Remove duplicates
l=[10,20,30,40,50,10]
a=[]
for i in l:
    if i not in a:
        a.append(i)
print(a)
#Factorial
n=int(input("Enter the number: "))
f=1
for i in range(1,n+1):
    f=f*i
print(f)
#sum of natural umbers
n=int(input("Enter the number: "))
s=0
for i in range(1,n+1):
    s=s+i
print(s)
#check even or odd
n=int(input("Enter the number: "))
if n%2==0:
    print("It is even")
else:
    print("It is odd")
 


