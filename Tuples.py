#methods
#index
t = (1,2,3,4,5)
i = t.index(3)
print(i)

#count
t = (1,2,2,3,4,2)
c = t.count(2)
print(c)

t = (1,2,3,4,5)
print(t[3])

#slicing
t = (1,2,3,4,5,6)
print(t[1:3])

#unpacking
t = (1,2,3)
a,b,c = t
print(a,b,c)

#concatenation
t1= (1,2,3)
t2 = (4,5,6)
print(t1 + t2)

#length
a = (1,2,3,4,5)
print(len(a))

#max
a = (1,2,3,4,5,6)
print(max(a))

#min
a = (1,2,3,4,5,6)
print(min(a))

comparision
a = (1,2,3)
b = (1,2,4)
print(a<b)
