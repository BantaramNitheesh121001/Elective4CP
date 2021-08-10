# Write the function setKthDigit(n, k, d) that takes three integers -- n, k, and d 
# where n is a possibly-negative int, k is a non-negative int, and d is a non-negative 
# single digit (between 0 and 9 inclusive). This function returns the number n with 
# the kth digit replaced with d. Counting starts at 0 and goes right-to-left, 
# so the 0th digit is the rightmost digit. 



def fun_set_kth_digit(n, k, d):
	s = n 
	n = str(abs(n))
	if len(n) >= k:
		n = n[::-1]
		n = n[:k] + str(d) + n[k+1:]
		n = int(n[::-1])
	else:
		n = d*(10**k)+int(n)
	if s < 0 :
		return -n
	else:
		return n
		
# print(fun_set_kth_digit(-468, 2, 1))