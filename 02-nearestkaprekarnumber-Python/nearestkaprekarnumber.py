# Note: please do not start this problem prior to completing previous problem. 
# Bearing in mind the definition of Kaprekar Number from above problem, write the function 
# nearestKaprekarNumber(n) that takes an int value n and returns the Kaprekar number 
# closest to n, with ties going to smaller value. For example, nearestKaprekarNumber(49) returns 45, 
# and nearestKaprekarNumber(51) returns 55. And since ties go to the smaller number, 
# nearestKaprekarNumber(50) returns 45. 
# Note: as you probably guessed, this also cannot be solved by counting up from 0, 
# as that will not be efficient enough to get past the autograder. 
# Hint: one way to solve this is to start at n and grow in each direction until you find a Kaprekar number.



import math

l=[1]
 
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


def fun_nearestkaprekarnumber(n):
    if n in l:
        return n 
    s=n
    for i in range(len(l)):
        if(abs(n-l[i])<s):
            s=n-l[i]
    return abs(n-s)