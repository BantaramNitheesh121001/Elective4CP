# Happy Primes [20 pts]
# Background: read the first paragraph from the Wikipedia page on happy numbers. After 
# some thought, we see that no matter what number we start with, when we keep replacing 
# the number by the sum of the squares of its digits, we'll always either arrive at 4 (
# unhappy) or at 1 (happy). With that in mind, we want to write the function nthHappyNumber
# (n). However, to write that function, we'll first need to write isHappyNumber(n) (
# right?). And to write that function, we'll first need to write sumOfSquaresOfDigits(n). 
# And that's top-down design! Here we go.... 
# Note: the autograder will grade each of the following functions, so they are required. 
# However, they also are here specifically because they are just the right helper 
# functions to make nthHappyNumber(n) easier to write!

def ishappyprimenumber(n):
    dummy = n
    if n < 0:
        return False
    while True:
        n = sq(n)
        if n == 1 and prime(dummy):
            return True
        if n < 10:
            return False

def sq(n):
    val = 0
    while True:
        if n == 0:
            return val
        val += (n%10)**2
        n = n//10

def prime(n):
	if n < 2:
		return False
	if n == 2:
		return True
	for i in range (3,n):
		if n % 2 == 0:
			return False
		if n % i == 0:
			return False
	return True

prime(ishappyprimenumber(833))