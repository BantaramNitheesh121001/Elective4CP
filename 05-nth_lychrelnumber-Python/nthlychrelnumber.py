# nthLychrelNumber(n) [20 pts]
# A Lychrel number is a natural number that cannot form a palindrome through the iterative process of 
# repeatedly reversing its digits and adding the resulting numbers. This process is sometimes called the 
# 196-algorithm, after the most famous number associated with the process.
# The first few Lychrel numbers are 196, 295, 394, 493, 592, 689, 691, 788, 790, 879, 887….


def reverse(num):
    rnum = 0
    while(num>0):
        x = num%10
        rnum = rnum*10+x
        num = num//10
    return rnum

def check(num):
    rnum = reverse(num)
    if(rnum==num):
        return True
    else:
        return False

def nthlychrelnumbers(n):
    # your code goes here
    num = 196
    count = 0
    while(count<n):
        num1 = num
        for i in range(25):
            number = num1 + reverse(num1)
            val = check(number)
            if(val):
                break
            else:
                num1= number
                
        if(val==False):
            count= count+1
            num = num+1
        else:
            num = num+1

                
            
    return num-1