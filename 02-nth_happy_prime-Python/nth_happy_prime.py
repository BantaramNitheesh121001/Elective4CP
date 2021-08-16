# A happy prime is a number that is both happy and prime. 
# Write the function nthHappyPrime(n) which takes a non-negative integer 
# and returns the nth happy prime number (where the 0th happy prime number is 7).

def sq(n):
	val = 0
	while True:
		if n == 0:
			return val
		val += (n%10)**2
		n = n//10

def happy(n):
	while True:
		n = sq(n)
		if n == 1:
			return True
		if n < 10:
			return False

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

def fun_nth_happy_prime(n):
	count = 0
	i = 0
	while True:
		i += 1
		if happy(i) and prime(i):
			count += 1
		if count-1 == n:
			return i
print(fun_nth_happy_prime(1))