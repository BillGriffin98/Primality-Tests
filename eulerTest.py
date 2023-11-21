import random

subject = input("n = ")
trials = input("t = ")

def jacobi(a, p):
    if a == 0:
        return 0
    elif a == 1:
        return 1
    elif a % 2 == 0:
        return jacobi(a // 2, p) * ((-1) ** ((p ** 2 - 1) // 8))
    else:
        return jacobi(p % a, a) * ((-1) ** ((a - 1) * (p - 1) // 4))

def gcd(a,b):
    while b != 0:
        a, b = b, a % b
    return a

def eulerPrime(n):
    for i in range(1, int(trials) + 1):
        a = random.randrange(1,n)
        while gcd(a,n) != 1:
            a = random.randrange(1,n)
        b = pow(int(a), int((n - 1) / 2), int(n))
        if b!=0 and b!=1:
            b = b - n
        if b == jacobi(a,n):
                continue
        else:
            return False
    return ("prime with probability (1/2)ˆ"+str(trials))

print(eulerPrime(int(subject)))