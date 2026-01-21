#Check whether a number is Prime
def is_prime(num):
    if num<=1:
        return False
    for i in range(2,num):
        if num%i==0:
            return True
        return False
    