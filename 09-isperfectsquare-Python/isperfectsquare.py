# isPerfectSquare(n) [10pts]
# Write the function isPerfectSquare(n) that takes a possibly-non-int value, and returns True if
# it is an int that is a perfect square (that is, if there exists an integer m such that
# m**2 == n), and False otherwise. Do not crash on non-ints nor on negative ints.

def isperfectsquare(n):
	# your code goes here
	if ( type(n) is int and n < 0) or type(n) is float:
		return False
	if type(n) is int:
		val = n ** (1/2)
		if val*val == n:
			return True
	if type(n) is str and not n.isalpha():
		n = int(n)
		val = n ** (1/2)
		if val*val == n:
			return True
	else:
		return False
		
print(isperfectsquare(25))
