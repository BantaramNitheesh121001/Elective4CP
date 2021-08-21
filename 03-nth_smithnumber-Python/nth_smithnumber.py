# Write the function nthSmithNumber that takes a non-negative int n 
# and returns the nth Smith number, where a Smith number is a composite (non-prime) 
# the sum of whose digits are the sum of the digits of its prime factors (excluding 1). 
# Note that if a prime number divides the Smith number multiple times, its digit sum 
# is counted that many times. For example, 4 equals 2**2, so the prime factor 2 is 
# counted twice, thus making 4 a Smith Number.
# so fun_nthsmithnumber(0) should return 4
# so fun_nthsmithnumber(1) should return 22

def isprime(n):
    if n < 2:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

def sumofdigits(n):
    sum = 0
    while (n > 0):
        sum += (n % 10)
        n = n // 10
    return sum    


def smith(n):
    if(isprime(n)):
        return False
    if(sumofdigits(n) == primefactors(n)):
        return True
    return False

def primefactors(n):
    i = 2
    sum = 0
    l = []
    while i * i <= n:
        if n % i == 0:
            sum += sumofdigits(i)
            l.append(i)
            n //= i
        else:
            i += 1

    if n > 1:
        l.append(n)
        sum += sumofdigits(n)
    return sum
def fun_nth_smithnumber(n):
    count = 0
    i = 0
    while (count <= n):
        i += 1
        if smith(i):
            count += 1
    return i