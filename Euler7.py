import math
# we're starting from 5. so 2,3 are the primes
primeNumbersFound = 2
number = 5
findNthPrime = 10001


def isPrime(num):
    for i in range(2, math.ceil(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True


while primeNumbersFound < findNthPrime:
    if isPrime(number):
        primeNumbersFound += 1

    if primeNumbersFound == findNthPrime:
        print(number)
    # to omit even numbers
    number += 2
