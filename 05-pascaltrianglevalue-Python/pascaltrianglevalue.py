# Write the function pascalsTriangleValue(row, col) 
# that takes int values row and col, and returns the 
# value in the given row and column of Pascal's 
# Triangle where the triangle starts at row 0, and 
# each row starts at column 0. If either row or col 
# are not legal values, return None, instead of crashing. 


def fun_pascaltrianglevalue(row, col):
	a = []
	for i in range(row+1):
		a.append(0)
	a[0] = 1
	a[-1] = 1
	for i in range(1,len(a)-1):
		a[i] = a[i-1]*(row-i+1)//i

	print(a)
	if(len(a)<col):
		return 0
	else:
		return a[col]