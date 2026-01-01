#functions
def say_hello():
    print("Hello, welcome to Python!")
say_hello()
#add
def add(a, b):
    return a + b

print(add(5, 3))
#mul
def add(a, b):
    return a * b

print(add(3, 3))
#name
def welcome(name):
    print("Welcome,", name)

welcome("Lokesh")
#square
def square(n):
    return n * n

print(square(4))
#even or odd
def even_odd(n):
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")

even_odd(7)
#Given an array of integers nums, return the number of good pairs.A pair (i, j) is called good if nums[i] == nums[j] and i < j.
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count={}
        pairs=0
        for num in nums:
            if num in count:
                pairs+=count[num]
                count[num]+=1
            else:
                count[num]=1
        return pairs
        
