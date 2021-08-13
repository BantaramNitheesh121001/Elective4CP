# hasConsecutiveDigits(n)  [10pts]
# Write the function hasConsecutiveDigits(n) that takes a possibly negative int value n and returns True if that 
# number contains two consecutive digits that are the same, and False otherwise.

def hasconsecutivedigits(n):
	# your code goes here
	n = abs(n)
	if n < 10:
		return False
	while(True):
		if n < 9:
			break
		val = n%10
		n = n//10
		val1 = n%10
		if val == val1 or val == val1:
			return True
	return False