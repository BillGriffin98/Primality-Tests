import random

#User enters in the number to be tested along with how many bases they want to test the number with
subject = input("n = ")
trials = input("t = ")

#Define the Jacobi symbol
def jacobi(a, p):
    if a == 0:
        return 0
    elif a == 1:
        return 1
    elif a % 2 == 0:
        return jacobi(a // 2, p) * ((-1) ** ((p ** 2 - 1) // 8))
    else:
        return jacobi(p % a, a) * ((-1) ** ((a - 1) * (p - 1) // 4))

#Define the greatest common divisor 
def gcd(a,b):
    while b != 0:
        a, b = b, a % b
    return a


def eulerPrime(n):

    for i in range(1, int(trials) + 1): #Number of trials determines how often the test is repeated
        a = random.randrange(1,n) #Base is generated
        while gcd(a,n) != 1:
            a = random.randrange(1,n)
        b = pow(int(a), int((n - 1) / 2), int(n)) #Applies Euler's test
        if b!=0 and b!=1:
            b = b - n
        if b == jacobi(a,n):
                continue
        else:
            return False
    return ("prime with probability (1/2)ˆ"+str(trials)) #If the test doesn't detect a composite number, this tells the user the chances of their number being prime

print(eulerPrime(int(subject)))