"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def quicksort(array):
	# Your code goes here
	if len(array) > 1:
		pivot = array.pop()
		low = []
		high = []
		equal = [pivot]
		for i in array:
			if pivot == i:
				equal.append(i)
			elif pivot > i:
				high.append(i)
			else:
				low.append(i)
		return (quicksort(high)+equal+quicksort(low))
	else:
		return array

print(quicksort([21, 4, 1, 3, 9, 20, 25, 6, 21, 14]))