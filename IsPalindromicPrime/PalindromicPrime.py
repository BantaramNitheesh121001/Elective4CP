# isPalindromicPrime() Write a function isPalindromicPrime that takes a value n as a parameter and returns True if the given n is a palindrome and prime and False otherwise.

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

def Palindromic(n):
    check = n
    val = 0
    i = 0
    while True:
        if n == 0:
            break
        val += (n%10) / (10**i)
        n = n // 10
        i += 1
    val = int(val * (10**(i-1)))
    if check == val:
        return True
    return False

def isPalindromicPrime(n):
    if Palindromic(n) and prime(n):
        return True
    return False

print(Palindromic(2))