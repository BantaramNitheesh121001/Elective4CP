# isLatinSquare(a)
# Write the function isLatinSquare(a) that takes a 2d list 
# and returns True if it is a Latin square and False otherwise.

# Check for Latin square in the following link:
# https://en.wikipedia.org/wiki/Latin_square

# Write your own test cases...

def isLatinSquare(lst):
    # Your code goes here...
    for i in range (len(lst)):
        for j in range(len(lst[0])):
            if lst[i].count(lst[i][j]) > 1:
                return False

    for i in range (len(lst[0])):
        for j in range(len(lst)):
            if lst
            print (lst[j][i])
    return True

a =[[1,2,3],[4,5,6],[7,8,9]]
print(isLatinSquare(a))
# assert (isLatinSquare(a)==True)