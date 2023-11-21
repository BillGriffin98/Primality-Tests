subject = input("p = ")
print("M_" + subject + " = 2^" + subject + " - 1 = " + str(2**int(subject) - 1))

def LLTest(p): 
    s=4
    M_p = 2**p - 1
    for i in range(0, p - 2):
        s = (((s**2) - 2) % M_p)
    if s == 0:
        return ("Prime") 
    else:
        return ("Composite")

print(LLTest(int(subject)))