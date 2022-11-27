import random
from math import sqrt
from math import floor

#slow
def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    
    if num % 2 == 0:
        return False
    
    for n in range(3, floor(sqrt(num)) +1 ,2):
        if num % n == 0:
            return False
    return True

#using Fermat's Litle Theorem
def is_prime_v2(n, k = 10):
    if n <= 1:
        return False
    
    for _ in range(k):
        a = random.randint(2, n) - 1
        if pow(a, n, n) != a:
            return False
        
    return True

def get_factors(num):
    factors = []
    
    limit = sqrt(num)
    
    for n in range(2,floor(limit)):
        if num % n == 0:
            factors.append([n, num/n])
    return factors

#discrete logarithm
def discrete_logarithm(a,b,m):
    c = 1
    
    while pow(b,c) % m != a:
        c = c + 1
    return c


def modular_exponentiation(b,c,m):
    return pow(b,c) % m

if __name__ == '__main__':
    number = 5
    exp = 948603
    mod = 9048610007
    #print(modular_exponentiation(number,exp,mod))
    print(discrete_logarithm(3668993056,5,mod))