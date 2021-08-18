# IsAdditivePrime: Additive primes can be defined as prime numbers where the sum of its digits is a prime number. Write a function isAdditivePrime that takes n as an integer and returns True if n is an Additive Prime and False otherwise.Some of the Additive Primes are 2, 3, 5, 7, 11, 23, 29, and etc.
# 29 = 2 + 9 = 11 = 1 + 1 = 2 and 2 is a prime number.

def Additive(n):
    val = 0
    while True:
        if n == 0:
            if prime(val):
                return True
            return False
        val += n % 10
        n = n // 10


def prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    for i in range (2,n):
        if n % 2 == 0:
            return False
        elif n % i == 0:
            return False
    return True

def IsAdditivePrime(n):
    if Additive(n):
        return True
    return False

print (IsAdditivePrime(67))