subject = input("p = ") #Collects input from user
print("M_" + subject + " = 2^" + subject + " - 1 = " + str(2**int(subject) - 1))

#Defines the Lucas-Lehmer primality test
def LLTest(p): 
    s=4 #Initialises variable
    M_p = 2**p - 1 #Defines the Mersenne prime
    for i in range(0, p - 2): #Generates S_k up to the p'th term
        s = (((s**2) - 2) % M_p)
    if s == 0: #Performs the primality test
        return ("Prime") 
    else:
        return ("Composite")

print(LLTest(int(subject)))