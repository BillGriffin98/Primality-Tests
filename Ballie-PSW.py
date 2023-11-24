import random

#Defines the Miller-Rabin primality test
def millerRabin(n):
    temp = float(n) - 1
    e = 0
    while temp % 2 == 0: #Determines e and k such that n - 1 = 2^e * k
        e = e + 1
        temp = temp / 2
        continue
    k = (float(n) - 1) / (2**e)
    a = random.randrange(2, float(n))
    listOfWitnesses = []

    for i in range(e + 1):
        if i == 0:
            if pow(a, int(k), int(n)) != 1: #Determines if a^k % 0 != 1 (mod n) 
                listOfWitnesses.append(pow(a, int(k), int(n))) #If so, then the number may be composite we add it to our sequence
                continue
            else:
                return True
        else:
            if pow(a, int(k*(2**i)), int(n)) != -1:
                listOfWitnesses.append(pow(a, int(k*(2**i)), int(n)))
                continue
            else:
                return True
    print(listOfWitnesses) #Returns our Miller-Rabin sequence that varifies the number is indeed composite
    return False

#Defines the greatest common divisor
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

#Defines the Jacobi symbol
def jacobi(a, p):
    if a == 0:
        return 0
    elif a == 1:
        return 1
    elif a % 2 == 0:
        return jacobi(a // 2, p) * ((-1) ** ((p ** 2 - 1) // 8))
    else:
        return jacobi(p % a, a) * ((-1) ** ((a - 1) * (p - 1) // 4))

#Defines the Lucas primality test
def isLucasPrime(n):
    dAbs, sign, d = 5, 1, 5
    while 1:
        if 1 < gcd(d, n) < n:
            return False
        if jacobi(d, n) == -1:
            break
        dAbs, sign = dAbs + 2, sign * -1
        d = dAbs * sign
    
    p, q = 1, (1 - d) // 4
    u, v, u2, v2, q, q2 = 0, 2, 1, p, q, 2 * q
    bits = []
    t = (n + 1) // 2
    
    while t > 0:
        bits.append(t % 2)
        t = t // 2
    
    h = 0
    while h < len(bits):
        u2 = (u2 * v2) % n
        v2 = (v2 * v2 - q2) % n
        if bits[h] == 1:
            uold = u
            u = (u2 * v + u * v2) % n
            u = u if u % 2 == 0 else u + n
            u = (u // 2) % n
            v = (v2 * v + u2 * uold * d) % n
            v = v if v % 2 == 0 else v + n
            v = (v // 2) % n
        if h < len(bits) - 1:
            q = (q * q) % n
            q2 = q + q
        h = h + 1
    
    return u == 0


#Performs the Ballie-PSW 
def balliePsw(n):
    if isLucasPrime(n) == False: #Performs the Lucas test
        return False
    if millerRabin(n) == False: #Performs the Miller-Rabin test
        return False
    else:
        return True #If n passes both, then it is almost certainly prime


subject = int(input("n = "))

print(balliePsw(subject))
