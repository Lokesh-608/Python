#Check whether a number is Prime
num = int(input("Enter a number: "))

if num <= 1:
    print("It is not prime")
else:
    for i in range(2, num):
        if num % i == 0:
            print("It is not prime")
            break
    else:
        print("It is prime")
#Check Palindrome Number
num =int(input("Enter the number: "))
n = str(num)
if n == n[::-1]:
    print("It is palindrome")
else:
    print("It is not palindrome")
     

