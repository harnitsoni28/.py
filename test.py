import math
def checkPrime(n):
    if n < 2:
        return False

    for i in range(2, int(math.sqrt(n))+1): 
        if n % i == 0:
            return False

    return True


left = int(input("Lower Value: "))
right = int(input("Upper Value: "))



for num in range(left, right):
    if checkPrime(num):
        print (num)

