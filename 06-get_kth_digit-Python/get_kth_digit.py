# Write the function getKthDigit(n, k) that takes 
# a possibly-negative int n and a non-negative int k, 
# and returns the kth digit of n, starting from 0, counting from the right.
# if the kth digit is not present return 0 



def fun_get_kth_digit(digit, k):
	digit = abs(digit)
	i = 0
	while True:
		val = digit % 10
		digit = digit // 10
		if i == k:
			return val
		if digit == 0:
			return 0
		i += 1
print (fun_get_kth_digit(-789,0))