from sympy import randprime
from sympy.ntheory.residue_ntheory import primitive_root
from random import randint
from math import gcd as bltin_gcd

def coprime2(a, b):
    return bltin_gcd(a, b) == 1

##def primRoots(modulo):
##    g = 2
##    l = list(factorint(modulo-1).keys())
##    lw = len(l)
##    m = modulo - 1
##    mods = []
##    ini = True
##    while ini:
##        for prime in l:
##            mods.append(pow(g,int(m/prime),modulo))
##
##
##        if 1 in mods:
##            mods = []
##            g+=1
##            while (coprime2(g,m) == False):
##                g += 1
##        else:
##            if coprime2(g,m) == True:
##                ini = False
##            else:
##                g+=1
##    return g


def genSecret(prime):
    start = randint((prime - 1)/2,prime-1)
    while coprime2(start,(p-1)) == False:
        start += 1
    return start

menu = input("Would you like to generate a new key (G) or accept a key (A)? ")

if menu == "G":
    seed = input("Please input a large integer as a seed. ")
    p = randprime(int(seed),2*int(seed))
    g = primitive_root(p)
    print("Tell your partner that p = " + str(p) + " and g = " + str(g))
    a = genSecret(p)
    print("Tell your partner that your unlocked key is " + str(pow(g,a,p)))
    B = input("What is your partners unlocked key? ")
    pw = pow(int(B),a,p)
    print("Password is " + str(pw))


elif menu == "A":
    p = input("What is the value of p? ")
    g = input("What is the value of g? ")
    p = int(p)
    g = int(g)
    g = primRoots(p)
    b = genSecret(p)
    print("Tell your partner that your unlocked key is " + str(pow(g,b,p)))
    A = input("What is your partners unlocked key? ")
    print("The password is " + str(pow(int(A),b,p)))


else:
    print("No correct option given.")
