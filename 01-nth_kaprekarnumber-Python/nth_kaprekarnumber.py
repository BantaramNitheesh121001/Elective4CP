# Background: a Kaprekar number is a non-negative integer, the representation of whose square 
# can be split into two possibly-different-length parts (where the right part is not zero) 
# that add up to the original number again. For instance, 45 is a Kaprekar number, because 
# 45**2 = 2025 and 20+25 = 45. You can read more about Kaprekar numbers here. The first several 
# Kaprekar numbers are: 1, 9, 45, 55, 99, 297, 703, 999 , 2223, 2728,... 
# With this in mind, write the function nthKaprekarNumber(n) that takes a non-negative int n 
# and returns the nth Kaprekar number, where as usual we start counting at n==0.


import math

l = [1]
def fun_nth_kaprekarnumber(n):
    return l[n]
def print_Kaprekar_nums(start, end):  
   for i in range(start, end):  
      sqr = i ** 2  
      digits = str(sqr)  
  
      length = len(digits)  
      for x in range(1, length):  
         left = int("".join(digits[:x]))  
         right = int("".join(digits[x:]))  
         if ((left + right) == i):
            if(str(i)[0]!='1' or str(i)[1:]!='0'*(len(str(i))-1)):  
                    l.append(i)  

print_Kaprekar_nums(1, 100000)