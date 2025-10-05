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
#power of two
n = int(input("Enter a number: "))
for i in range(31):
    if n == 2 ** i:
        print(True)
        break
else:
    print(False)
#power of three
n = int(input("Enter a number: "))
for i in range(31):
    if n == 3 ** i:
        print(True)
        break
else:
    print(False)
#power of four
n = int(input("Enter a number: "))
for i in range(31):
    if n == 4 ** i:
        print(True)
else:
    print(False)
 where answer[i] = |leftSum[i] - rightSum[i]|.
nums = [10,4,8,3]
ans = []
one = []
two = []
res = 0
res1 = 0
for i in range(len(nums)):
    if i == 0:
        one.append(0)
    else:
        res += nums[i-1]
        one.append(res)
for i in range(len(nums)-1,-1,-1):
    if i == len(nums)-1:
        two.append(0)
    else:
        res1 += nums[i+1]
        two.append(res1)
two.reverse()
for i in range(len(one)):
    ans.append(abs(one[i] - two[i]))
print(ans)
# 67. Add Binary
# Given two binary strings x and y, return their sum as a binary string.
x= "11"
y= "1"
num1 = int(x,2)
num2 = int(y,2)
print(bin(num1 + num2)[2:])
#power of three
n = int(input("Enter a number: "))
for i in range(31):
    if n == 3 ** i:
        print(True)
        break
else:
    print(False)
# Find the index of 'cherry' in the tuple (‘apple’, ‘banana’, ‘cherry’, ‘apple’).
tup = ('apple', 'banana', 'cherry', 'apple')
for i in range(len(tup)):
    if tup[i] == 'cherry':
        print(i)
# Create a tuple with different data types (string, int, float, bool). Print each element with its type.
tup1 = ("Ashritha",30,50.68,True)
for i in tup1:
    print(type(i))
print(tup1)
#

