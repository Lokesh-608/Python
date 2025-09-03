#data types
# Numeric data type
#Take two numbers and find their sum, difference, product, and division.
a = 20
b = 10
c = a+b
print(c)

d = a - b
e = a*b
f = a/b
print(d)
print(e)
print(f)
#Convert a float number into an integer.
a = 10.2
b = int(a)
print(b)
#Swap two numbers without using a third variable.
a,b = 10,20
a,b = b,a
print(a,b)

#Strings
#Take a string and find its length using len().
a = "Lokesh"
print(len(a))

#Convert a string into uppercase and lowercase.

a = "LOKESH"
print(a.lower())

#Concatenate two strings without using + (use .join).
a = "Lokesh"
b = "Reddy"
c = "{} {}".format(a,b)
print(c)

#Extract the first three and last three characters of a string.
a = "Python is good"
print(a[0])
print(a[1])
print(a[2])
print(a[-1])
print(a[-2])
print(a[-3])

#Lists
#Create a list of 5 numbers and find the maximum and minimum values.
a = ["1","2","3","4","5"]
c = max(a)
d = min(a)
print(c)
print(d)
#Find the sum of all elements in a list using sum().
a = [1,2,3,4,5]
c = sum(a)
print(c)

#Sort a list in ascending and descending order.
numbers = [5, 2, 9, 1, 7]
numbers.sort()
print("Ascending:", numbers)

number = [5, 2, 9, 1, 7]
number.sort(reverse=True)
print("descending:", number) 
#Tuples
#Create a tuple and access the third element.
t = (10, 20, 30, 40, 50)
print(t[2])
#Convert a list into a tuple and vice versa.
l = [1, 2, 3, 'a', 'b']
t = tuple(l)
print(t)
print(type(t))
#Sets
#Create two sets and find their union, intersection, and difference.
a = {1,2,3,4,5}
b = {4,5,6,7}
c = a.union(b)
print(c)
d = a.intersection(b)
print(d)
f = a.difference(b)
print(f)

#Dictionaries
#Create a dictionary with 3 key-value pairs and print the keys.
d = {"1":"loki","2":"ashri","3":"varun"}
print(d["1"])
print(d["2"])
print(d["3"])

#Update the value of a dictionary key.
d["1"] = "lokesh"
print(d)
c = d.keys()
print(c)
c = d.values()
print(c)