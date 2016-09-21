# By Dimitris_GR from forums
# Modify Problem Set 31's (Optional) Symmetric Square to return True
# if the given square is antisymmetric and False otherwise.
# An nxn square is called antisymmetric if A[i][j]=-A[j][i]
# for each i=0,1,...,n-1 and for each j=0,1,...,n-1.


def antisymmetric(p):
    i = 0
    while i < len(p):
        if len(p) != len(p[i]):
            return False
        j = 0
        while j < len(p[i]):
            if p[i][j] != -p[j][i]:
                return False
            j += 1
        i += 1
    return True

# Test Cases:

print(antisymmetric([[0, 1, 2],
                     [-1, 0, 3],
                     [-2, -3, 0]]))
#>>> True

print(antisymmetric([[0, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0]]))
#>>> True

print(antisymmetric([[0, 1, 2],
                     [-1, 0, -2],
                     [2, 2,  3]]))
#>>> False

print(antisymmetric([[1, 2, 5],
                     [0, 1, -9],
                     [0, 0, 1]]))
#>>> False


print('##################################################')
##########################################################


# By Ashwath from forums
# Given a list of lists representing a n * n matrix as input,
# define a  procedure that returns True if the input is an identity matrix
# and False otherwise.

# An IDENTITY matrix is a square matrix in which all the elements
# on the principal/main diagonal are 1 and all the elements outside
# the principal diagonal are 0.
# (A square matrix is a matrix in which the number of rows
# is equal to the number of columns)


def is_identity_matrix(p):
    i = 0
    while i < len(p):
        if len(p) != len(p[i]):
            return False
        j = 0
        while j < len(p[i]):
            if i == j and p[i][j] != 1:
                return False
            elif i != j and p[i][j] != 0:
                return False
            j += 1
        i += 1
    return True


# Test Cases:

matrix1 = [[1,0,0,0],
           [0,1,0,0],
           [0,0,1,0],
           [0,0,0,1]]
print(is_identity_matrix(matrix1))
# >>>True

matrix2 = [[1,0,0],
           [0,1,0],
           [0,0,0]]

print(is_identity_matrix(matrix2))
# >>>False

matrix3 = [[2,0,0],
           [0,2,0],
           [0,0,2]]

print(is_identity_matrix(matrix3))
# >>>False

matrix4 = [[1,0,0,0],
           [0,1,1,0],
           [0,0,0,1]]

print(is_identity_matrix(matrix4))
# >>>False

matrix5 = [[1,0,0,0,0,0,0,0,0]]

print(is_identity_matrix(matrix5))
# >>>False

matrix6 = [[1,0,0,0],
           [0,1,0,1],
           [0,0,1,0],
           [0,0,0,1]]

print(is_identity_matrix(matrix6))
# >>>False

matrix7 = [[1, -1, 1],
           [0, 1, 0],
           [0, 0, 1]]
print(is_identity_matrix(matrix7))
# >>>False


print('##################################################')
##########################################################


# Numbers in lists by SeanMc from forums
# define a procedure that takes in a string of numbers from 1-9 and
# outputs a list with the following parameters:
# Every number in the string should be inserted into the list.
# If a number x in the string is less than or equal
# to the preceding number y, the number x should be inserted
# into a sublist. Continue adding the following numbers to the
# sublist until reaching a number z that
# is greater than the number y.
# Then add this number z to the normal list and continue.

# Hint - "int()" turns a string's element into a number

def numbers_in_lists(string):
    final = [string[0]]
    sublist = []
    y = string[0]
    i = 1
    while i < len(string):
        if string[i] < string[i - 1]:
            sublist += string[i]
        else:
            final.append(sublist)
            sublist = []
        i += 1
    return final

# testcases

string = '543987'
result = [5,[4,3],9,[8,7]]
print(repr(string), numbers_in_lists(string) == result)

string= '987654321'
result = [9,[8,7,6,5,4,3,2,1]]
print(repr(string), numbers_in_lists(string) == result)

string = '455532123266'
result = [4, 5, [5, 5, 3, 2, 1, 2, 3, 2], 6, [6]]
print(repr(string), numbers_in_lists(string) == result)

string = '123456789'
result = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(repr(string), numbers_in_lists(string) == result)
