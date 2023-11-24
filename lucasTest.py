def gcd(a, b): #Defines the greatest commmon divisor of two numbers a, b.
    while b != 0:
        a, b = b, a % b
    return a

def jacobi(a, p): #Defines the Jacobi symbol for two numbers a, p.
    if a == 0:
        return 0
    elif a == 1:
        return 1
    elif a % 2 == 0:
        return jacobi(a // 2, p) * ((-1) ** ((p ** 2 - 1) // 8))
    else:
        return jacobi(p % a, a) * ((-1) ** ((a - 1) * (p - 1) // 4))

def isLucasPrime(n):

    #Find the value D for our Lucas sequence

    dAbs, sign, d = 5, 1, 5 #Initilising variables 

    while 1: #Tests if our current D gives the correct gcd and jacobi. If not, then we move to the next D in the sequence {5, -7, 9, -11, 13,...}
        if 1 < gcd(d, n) < n: 
            return False
        if jacobi(d, n) == -1:
            break
        dAbs, sign = dAbs + 2, sign * -1
        d = dAbs * sign
    
    
    #Computing our Lucas sequence

    p, q = 1, (1 - d) // 4 #Initialising variables
    u, v, u2, v2, q, q2 = 0, 2, 1, p, q, 2 * q

    bits = [] #Generating a binary representation of (n+1)/2 
    t = (n + 1) // 2
    while t > 0:
        bits.append(t % 2)
        t = t // 2
    
    h = 0 #Generate U_(n+1) in accordance with the binary representation
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

subject = input("n = ")
print(isLucasPrime(int(subject)))