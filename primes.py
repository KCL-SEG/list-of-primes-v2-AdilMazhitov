"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    primeNumber = 2
    if (number_of_primes) < 1:
        raise ValueError(f"{number_of_primes} should have been a positive number.")
    while (len(list) < int(number_of_primes)):
        counter = 0
        for i in range(1, primeNumber+1):
            if primeNumber % i == 0:
                counter += 1
        
        if (counter == 2):
            list.append(primeNumber)

        primeNumber += 1 

    return list

primes(10)