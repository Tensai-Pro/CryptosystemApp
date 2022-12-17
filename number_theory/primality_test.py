import math
import random
import number_theory.number_theory as nt

rnd = random.Random()

# Test Ferma for checking if a number is prime
def ferma(candidate):
    if candidate == 2:
        return True

    for i in range(100):
        a = (rnd.randint(0, 10000) % (candidate - 2)) + 2
        
        if nt.gcd(a, candidate) != 1:
            return False
        
        if pow(a, candidate-1, candidate) != 1:
            return False

    return True

# Miller-Rabin test for checking if a number is prime
def miller_rabin_test(candidate):
    print('Taking Miller-Rabin test...')
    """
    Miller-Rabin primality test.

    A return value of False means n is certainly not prime. A return value of
    True means n is very likely a prime.
    """
    if candidate != int(candidate):
        return False
    candidate = int(candidate)

    #Miller-Rabin test for prime
    if candidate == 0 or candidate == 1 or candidate == 4 or candidate == 6 or candidate == 8 or candidate == 9:
        return False
        
    if candidate == 2 or candidate == 3 or candidate == 5 or candidate == 7:
        return True

    maxDivisionsByTwo = 0
    evenNumber = candidate - 1
    while evenNumber % 2 == 0:
        evenNumber >>= 1
        maxDivisionsByTwo += 1
    assert(2 ** maxDivisionsByTwo * evenNumber == candidate-1)
  
    def trial_composite(a):
        if pow(a, evenNumber, candidate) == 1:
            return False
        for i in range(maxDivisionsByTwo):
            if pow(a, 2**i * evenNumber, candidate) == candidate-1:
                return False
        return True  
 
    numberOfRabinTrials = 10
    for i in range(numberOfRabinTrials):
        a = rnd.randrange(2, candidate)
        if trial_composite(a):
            return False
 
    return True

def is_prime(candidate):
    if candidate <= 1 or type(candidate) != int:
        return False
    if candidate in [2, 3, 5, 7]:
        return True
    if candidate in [4, 6, 8, 9, 10]:
        return False

    if candidate % 2 == 0 or candidate % 3 == 0:
        return False

    if candidate <= 5000:
        for i in range(5, int(math.sqrt(candidate))+1, 2):
            if candidate % i == 0:
                return False
        else:
            return True
    else:
        return miller_rabin_test(candidate)