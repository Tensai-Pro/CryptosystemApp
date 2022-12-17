import random
import math
import number_theory.primality_test as pt

rnd = random.SystemRandom()

def random_prime(bit):
    num = 0
    while True:
            num = nBit_random(bit)
            if not pt.is_prime(num):
                continue
            else:
                break
    return num
    
def nBit_random(bit):
    return rnd.randrange(2 ** (bit - 1) + 1 , 2 ** bit - 1)

def random_max(max):
    return rnd.randint(1, max)

# Euclede algorithm from wikipedia
def gcd(x, y):
    while(y):
       x, y = y, x % y
    
    return abs(x)

def coprime_number(number):
    if type(number) != int or number < 1:
        return
    
    for i in range(2, number):
        if gcd(number, i) == 1:
            return i

# function return a list of all prime factors (простые множители) of a given number
def prime_factors(num):
    if num <= 1 or type(num) != int:
        print('Wrong argument!')
        return
    if pt.is_prime(num): # meaning 0 prime factors
        return None

    factors = []
    while num % 2 == 0: # if n is even
        num = num // 2
        if 2 not in factors:
            factors.append(2)
    
    #now n is odd
    for i in range(3, int(math.sqrt(num))+2, 2):
        while num % i == 0: 
            if i not in factors:
                factors.append(i) 
            num = num // i
    
    if num > 2:
        if num not in factors:
            factors.append(num)
    
    return factors

def primitive_root(num, allRoots = False):
    if num <= 1 or type(num) != int:
        print('Wrong argument!')
        return

    if pt.is_prime(num):
        fi = num - 1    # fi function (функция эйлера)
        factors = prime_factors(fi)
        powers = [(fi // f) for f in factors] # powers for testing
        # roots = [] # list of primitive roots

        for g in range(2, num):
            for power in powers:
                if pow(g, power, num) == 1:
                    break
            else:
                return g
        else:
            print("No primitive roots found")
            return None
    else:
        print("It's not a prime number")
        return