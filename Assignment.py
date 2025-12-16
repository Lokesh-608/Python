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

