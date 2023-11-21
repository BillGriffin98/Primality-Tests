subject = input("n = ") #User inputs number to be tested for primality

def fermatTest(n):
    if (2**(float(n) - 1)) % float(n) == 1: #Computes a calculation derived from Fermat's Little Theorem to determines if a number is composite
        return True
    else:
        return False
    
print(fermatTest(subject))