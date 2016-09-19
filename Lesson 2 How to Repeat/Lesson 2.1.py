# Define a procedure, square, that takes one number
# as its input, and returns the square of that
# number (result of multiplying
# the number by itself).
# To help you out, the code for sum(a,b) is below.

def square(a):
    c = a * a
    return c

# To test your procedure, uncomment the print
# statement below, by removing the hash mark (#)
# at the beginning of the line.

# Do not remove the # from in front of the line
# with the arrows (>>>). Lines which begin like
# this (#>>>) are included to show the results
# you should see when run your procedure.

print (square(5))
#>>> 25

################################################################

# Define a procedure, find_second, that takes
# two strings as its inputs: a search string
# and a target string. It should return a
# number that is the position of the second
# occurrence of the target string in the
# search string.

def find_second(search_string, target_string):
    first_entry = search_string.find(target_string)
    return search_string.find(target_string, first_entry + 1)

danton = "De l'audace, encore de l'audace, toujours de l'audace"
print (find_second(danton, 'audace'))
#>>> 25

twister = "she sells seashells by the seashore"
print (find_second(twister,'she'))
#>>> 13

################################################################

# Define a procedure, bigger, that takes in
# two numbers as inputs, and returns the
# greater of the two inputs.

def bigger(a, b):
    if a > b:
        return a
    else:
        return b



print (bigger(2,7))
#>>> 7

print (bigger(3,2))
#>>> 3

print (bigger(3,3))
#>>> 3

###############################################################

# Define a procedure, is_friend, that
# takes a string as its input, and
# returns a Boolean indicating if
# the input string is the name of
# a friend. Assume I am friends with
# everyone whose name starts with D
# and no one else. You do not need to
# check for the lower case 'd'

def is_friend(name):
    return name[0] == 'D'


print (is_friend('Diane'))
#>>> True

print (is_friend('Fred'))
#>>> False

###############################################################

# Define a procedure, is_friend, that takes
# a string as its input, and returns a
# Boolean indicating if the input string
# is the name of a friend. Assume
# I am friends with everyone whose name
# starts with either 'D' or 'N', but no one
# else. You do not need to check for
# lower case 'd' or 'n'

def is_friend(name):
    if name[0] == 'D':
        return True
    else:
        if name[0] == 'N':
            return True
        else:
            return False

print (is_friend('Diane'))
#>>> True

print (is_friend('Ned'))
#>>> True

print (is_friend('Moe'))
#>>> False

#################################################################

# Define a procedure, biggest, that takes three
# numbers as inputs and returns the largest of
# those three numbers.

def biggest(a, b, c):
    if (a >= b) == (a >= c) == True:
        return a
    else:
        if (b >= a) == (b >= c) == True:
            return b
        else:
            return c


print (biggest(3, 6, 9))
#>>> 9

print (biggest(6, 9, 3))
#>>> 9

print (biggest(9, 3, 6))
#>>> 9

print (biggest(3, 3, 9))
#>>> 9

print (biggest(9, 3, 9))
#>>> 9

print (biggest(2, 2, 1))
#>>> 2

###############################################################

# Define a procedure, biggest, that takes three
# numbers as inputs and returns the largest of
# those three numbers.

def bigger(a, b):
    if a > b:
        return a
    else:
        return b

def biggest(a, b, c):
    return bigger(bigger(a, b), c)


print (biggest(3, 6, 9))
#>>> 9

print (biggest(6, 9, 3))
#>>> 9

print (biggest(9, 3, 6))
#>>> 9

print (biggest(3, 3, 9))
#>>> 9

print (biggest(9, 3, 9))
#>>> 9

print (biggest(2, 2, 1))
#>>> 2

###############################################################

# Define a procedure, print_numbers, that takes
# as input a positive whole number, and prints
# out all the whole numbers from 1 to the input
# number.

# Make sure your procedure prints "upwards", so
# from 1 up to the input number.

def print_numbers(a):
    i = 1
    while i <= a:
        print (i)
        i =  i + 1

print_numbers(3)
#>>> 1
#>>> 2
#>>> 3

############################################################

# Define a procedure, factorial, that
# takes one number as its input
# and returns the factorial of
# that number.

def factorial(n):
    a = 1
    fact = n
    while a < n:
        fact = fact * (n - a)
        a = a + 1
    return fact

print (factorial(4))
#>>> 24
print (factorial(5))
#>>> 120
print (factorial(6))
#>>> 720