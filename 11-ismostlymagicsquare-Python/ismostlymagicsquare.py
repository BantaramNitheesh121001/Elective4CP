# isMostlyMagicSquare(a) [15 pts]
# Write the function isMostlyMagicSquare(a) that takes an 2d list of numbers, which you may assume is an NxN square 
# with N>0, and returns True if it is "mostly magic" and False otherwise, where a square is "mostly magic" if:
# Each row, each column, and each of the 2 diagonals each sum to the same total.
# A completely magic square has additional restrictions (such as not allowing duplicates, and only allowing numbers 
# from 1 to N2), which we are not enforcing here, but which you can read about here. Note: any magic square is also 
# a "mostly magic" square, including this sample magic square:
# Read for more: https://en.wikipedia.org/wiki/Magic_square
# Here is another mostly-magic square:
# [ [ 42 ]]
# That square is 1x1 and each row, column, and diagonal sums to 42! And finally, here is a not-mostly-magic square:
# [ [ 1, 2],
#   [ 2, 1]]
# Each row and each column add to 3, but one diagonal adds to 2 and the other to 4.

def add(a):
	val = 0
	for i in a:
		val += i
	return val

def diagonal1(a):
	val = 0
	for i in range(len(a)):
		for j in range (len(a)):
			if i == j:
				val += a[i][j]
	return int(val)

def diagonal2(a):
	val = 0
	n = len(a)
	for i in range(n):
		for j in range (n):
			if i+j == n-1:
				val += a[i][j]
	return int(val)

def ismostlymagicsquare(a):
	# Your code goes here
	check = int(add(a[0]))
	for i in a:
		print(add(i))
		if check != add(i):
			return False

	for i in range (len(a)):
		value = 0
		for j in range (len(a[i])):
			value += a[j][i]
		print (value)
		if value != check:
			return False
	print (diagonal1(a),diagonal2(a))
	if check == diagonal1(a) and check == diagonal2(a):
		return True
	return False

a = [[16, 3, 2, 13], [5, 10, 11, 8], [9, 6, 7, 12],[4, 15, 14, 1]]
print (ismostlymagicsquare(a))
