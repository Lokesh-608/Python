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
#A school is trying to take an annual photo of all the students. The students are asked to stand in a single file line in non-decreasing order by height. Let this ordering be represented by the integer array expected where expected[i] is the expected height of the ith student in line.You are given an integer array heights representing the current order that the students are standing in. Each heights[i] is the height of the ith student in line (0-indexed).Return the number of indices where heights[i] != expected[i].
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        count = 0
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                count += 1
        return count
#Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

class solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        a=[]
        for i in nums:
            a.append(i*i)
        a.sort()
        return a

#circle area

 


