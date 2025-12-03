#loops
n = 5
for i in range(0, n):
    print(i)
#list
li = ["lokesh", "varun", "ram"]
for i in li:
    print(i)
#tuple
t = ("apple", "mango", "pineapple")
for i in t:
    print(i)
#string
l = "lokesh"
for i in l:
    print(i)
#break
i = [1,2,3,4]
for j in i:
    print(j)
    if j == 3:
        break

for x in range(2, 12, 3):
  print(x)
  #nested loop

for i in range(1, 5):
    for j in range(i):
        print(i, end=' ')
    print()

for i in range(1, 5):
    for j in range(i):
        print(i, end=' ') 
        print()
        #hello
for i in range(5):
    print("Lokesh")
    #power of four
    class Solution:
     def isPowerOfFour(self, n: int) -> bool:
        for i in range(31):
            if n == 4**i:
                return True
        return False
    #palindrome number
    x = int(input("Enter the number: "))
s = str(x)

if s == s[::-1]:
    print("True")
else:
    print("False")
#right triangle
n = 5
for i in range(1, n + 1):
    print("*" * i)
# triangle pattern 
#*
#**
#***
#****
#*****
n = 5
for i in range(5):
    for j in range(0,i+1):
        print("*", end="")  
    print()

#number triangle
#1
#12
#123
#1234
#12345
for i in range(0,5):
    for j in range(0,5):
        if(j<=i):
            print(j+1,end="")
    print()
#  #reverse number triangle
#54321
#5432
#543
#54
#5
n = 5
for i in range(n, 0, -1):
    for j in range(n, 0, 1):
        if(j>=i):
            print(j, end="")
    print()
#inverted triangle
#*****
#****
#***
#**
#*
n = 5
for i in range(n,0,1):
    for j in range(0,i):
        print("*", end="")
    print()
## 1
# 2 2 
# 3 3 3`    `
# 4 4 4 4
# 5 5 5 5 5
n = 5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end=" ")
    print()
print()
# 1
# 2 2 
# 3 3 3`    `
# 4 4 4 4
# 5 5 5 5 5
n = 5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end=" ")
    print()
print()
# 55555
# 4444
# 333
# 22
# 1

n = 5
for i in range(n,0,-1):
    for j in range(i):
        print(i,end=" ")
    print()
print()
#aaaaa
#aaaa
#aaa
#aa
#a
n = 6
for i in range(n, 0, -2):
    print('a' * i)
print()
#1
#12
#123
#1234
#12345
n = 5
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end='')
    print()
    #*
   #***
  #*****
 #*******
#*********
n = 5
for i in range(n):
    print(" " * (n - i - 1) + "*" * (2*i + 1))
# updated