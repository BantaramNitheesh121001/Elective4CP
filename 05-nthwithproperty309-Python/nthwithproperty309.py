# nthWithProperty309(n) [20 pts]
# We will say that a number n has "Property309" if its 5th power contains every 
# digit (from 0 to 9) at least once. 309 is the smallest number with this property. 
# Write the function nthWithProperty309 that takes a non-negative int n and returns 
# the nth number with Property309.

def nthwithproperty309(n):
	# Your code goes here
	count = -1
	i = 0
	while True:
		if property309(i):
			count += 1
		if count == n:
			break
		i = i + 1
	return i

def property309(n):
	a = n**5
	a = str(a)
	s = "1234567890"
	for i in s:
		if i not in a:
			return False
	return True