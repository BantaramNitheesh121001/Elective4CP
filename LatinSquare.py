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
    l = []
    for i in range (len(lst[0])):
        m = []
        for j in range(len(lst)):
            m.append(lst[j][i])
        l.append(m)
    for i in range (len(l)):
        for j in range(len(l[0])):
            if l[i].count(l[i][j]) > 1:
                return False
    return True

a =[[1,2,3],[2,3,1],[3,1,2]]
print(isLatinSquare(a))
assert (isLatinSquare(a)==True)
a = [[1, 2, 3, 4],[2, 1, 4, 3],[3, 4, 1, 2],[4, 3, 2, 1]]
assert (isLatinSquare(a)==True)
a = [[1, 2, 3, 2],[2, 1, 4, 3],[3, 4, 1, 2],[4, 3, 2, 1]]
assert (isLatinSquare(a)==False)
print("All Test Cases Passed")