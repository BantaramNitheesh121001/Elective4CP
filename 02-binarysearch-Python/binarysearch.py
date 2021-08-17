"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

def binary(input_array, value,low,high):
    if low < high:
        mid = low+(high-1)//2
        if value == input_array[mid]:
            return mid
        elif value > input_array[mid]:
            low = mid + 1
            return binary(input_array,value,low, high)
        else:
            high = mid - 1
            return binary(input_array,value, low, high)
    else:
        return -1

def binary_search(input_array, value):
    # Your code goes here
    low = 0
    high = len(input_array)-1
    return binary(input_array, value, low , high)
a = [1,3,9,11,15,19,29]
print(binary_search(a,25))