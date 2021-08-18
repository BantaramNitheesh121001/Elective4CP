# isSorted(a) (10 Pts)
# Write the function isSorted(a) that takes a list of numbers and returns True if the list 
# is sorted (either smallest-first or largest-first) and False otherwise. Your function 
# must only consider each value in the list once (so, in terms of big-oh, which we will 
# learn soon, it runs in O(n) time, where n=len(a)), and so in particular you may not sort 
# the list.

def issorted(a):
	# your code goes here
	n = len (a)
	if n == 0 or n == 1:
		return True
	if a[0] >= a[1]:
		for i in range (n):
			if i+1 == n:
				break
			if a[i] < a[i+1]:
				return False
		return True
	if a[0] <= a[1]:
		for i in range (n):
			if i+1 == n:
				break
			if a[i] > a[i+1]:
				return False
		return True

a = [1,1]
print(issorted(a))