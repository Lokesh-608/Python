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
