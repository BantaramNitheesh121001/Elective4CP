# Write the function matrixMultiply(m1, m2) that takes two 2d lists 
# (that we will consider to be matrices) and returns a new 2d list that 
# is the result of multiplying the two matrices. Return None if the 
# two matrices cannot be multiplied for any reason.


def fun_matrixmultiply(m1, m2):

    for i in range (len(m1)):
        if i == len(m1)-1:
            break
        if len(m1[i]) != len(m1[i+1]):
            return None

    for i in range (len(m2)):
        if i == len(m2)-1:
            break
        if len(m2[i]) != len(m2[i+1]):
            return None

    for i in range (len(m1)):
        if len(m1[i]) != len(m2):
            return None

    output = []
    for i in range (len(m1)):
        check = []
        for j in range (len(m2[0])):
            check.append(0)
        output.append(check)
    print (output)

    for i in range(len(m1)):
        for j in range(len(m2[0])):
            for k in range(len(m2)):
                output[i][j] += m1[i][k] * m2[k][j]
    return output
m1 = [[1,3],[2,4],[2,5]]
m2 = [[1,3,2,2], [2,4,5,1]]
print(fun_matrixmultiply(m1 , m2))