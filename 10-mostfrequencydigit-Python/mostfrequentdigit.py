# mostFrequentDigit(n) [10pts]
# Write the function mostFrequentDigit(n), that takes a non-negative integer n and returns the digit from 0 to 9 
# that occurs most frequently in it, with ties going to the smaller digit.

def mostfrequentdigit(n):
	# your code goes here
	x = n
	out = 0
	output = 0
	while True:
		if x == 0:
			break
		i = x%10
		x = x//10
		c = count(n,i)
		if c > out :
			out = c
			output = i
		elif c == out:
			if output > i:
				output = i 
	return output

def count(n,val):
	num = 0
	while True:
		if n == 0:
			break
		i = n%10
		n = n//10
		if val == i:
			num += 1
	return num

print(mostfrequentdigit(0))