#list collection of unordered collection
a = [1, 2, 3, 4, 5] 
b = ['lokesh', 'varun', 'praneeth'] 
c = [1, 'hello', 3.14, True] 
print(a)
print(b)
print(c)
#creating List with Repeated Elements
a = [2] * 5
b = [0] * 7
print(a)
print(b)
#Accessing List Elements
a = [10, 20, 30, 40, 50]
print(a[0])    
print(a[-1])
print(a[1:4])   

#sum and average
a =[10, 20, 30, 40, 50]
b = sum(a)
print(b)
c = b/5
print(c)
#largest number
a = [3, 9, 1, 7, 5]
b = max(a)
print(b)
c = min(a)
print(c)
print(len(a))
 #remove duplicate
a = [1, 2, 3, 4, 5, 5, 6]
b = list(set(a))
print(b)
 #indexing
a = [1, 2, 3, 4, 5]
i = a.index(3)
print(i)
#reverse list
a = [1,2,3,4]
a.reverse()
print(a)