import random

subject = input("n = ")

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



print(millerRabin(subject))