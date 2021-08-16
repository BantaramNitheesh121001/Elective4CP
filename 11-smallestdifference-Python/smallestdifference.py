# Write the function smallestDifference(a) that takes a list of integers and returns 
# the smallest absolute difference between any two 
# integers in the list. If the list is empty, return -1. For example:
#       assert(smallestDifference([19,2,83,6,27]) == 4)
# The two closest numbers in that list are 2 and 6, and their difference is 4.

def smallestdifference(a):
	# Your code goes here
	small = 0
	if len(a) == 0:
		return -1
	for i in range (len(a)):
		if i+1 == len(a):
			break
		for j in range (i+1,len(a)):
			val = abs(a[i] - a[j])
			if i == 0 and j == 1:
				small = val
			if val <= small:
				small = val
	return small

a = [19,2,83,6,27]
print(smallestdifference(a))