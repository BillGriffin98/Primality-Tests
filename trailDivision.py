import math
subject = input("n = ") #User inputs a number to be tested 

def trailDivision(n): #Defining a function that tests primality via trail division
    sqrtn = math.ceil(math.sqrt(float(n)))
    listOfNumbers = list(range(2, int(sqrtn + 1))) #Generates a list of numbers integers from 2 up to sqrt(n) + 1
    primes = [] #Initialises a list to store the primes we find within our list of numbers 
    
    while len(listOfNumbers) != 0: #Selects the lowest number from our list and removes all its multiples, leaving only primes
        p = listOfNumbers[0] 
        primes.append(p)
        listOfNumbers.remove(p)
        for i in listOfNumbers:
            if i % p == 0:
                listOfNumbers.remove(i)
            else:
                continue
    print(primes) #Trail divides our number by each prime from our list. If none are factors, we know our number is prime
    for j in range(1, len(primes) - 1):
        if float(n) % primes[j] == 0:
            return False
        else:
            continue
    return True

print(trailDivision(subject))

