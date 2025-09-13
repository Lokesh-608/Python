# Creating a Set in Python
set1 = {1, 2, 3, 4}
print(set1)

#set function
set1 = set("Python")
print(set1)

#creating list
s = set(["Lokesh", "varun", "ram"])
print(s)

#creating tuple
t = ("lokesh", "varun", "ram")
print(set(t))

#creating dictonary
d = {"Lokesh": 1, "varun": 2, "ram": 3}
print(set(d))

#Adding Elements to a Set in Python
s = {1,2,3,4}
s.add(5)
print(s)
#add multiple items
s = {1,2,3,4,5}
s.update([6,7])
print(s)