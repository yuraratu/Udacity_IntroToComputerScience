# Given the variable,

days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


# define a procedure, how_many_days,
# that takes as input a number
# representing a month, and returns
# the number of days in that month.


def how_many_days(month_number):
    return days_in_month[month_number - 1]


print(how_many_days(1))
# >>> 31

print(how_many_days(9))
# >>> 30


print('##################################################')
##########################################################


# Given the variable countries defined as:

#             Name    Capital  Populations (millions)
countries = [['China', 'Beijing', 1350],
             ['India', 'Delhi', 1210],
             ['Romania', 'Bucharest', 21],
             ['United States', 'Washington', 307]]

# Write code to print out the capital of India
# by accessing the list

print(countries[1][1])

# What multiple of Romania's population is the population
# of China? Calculate this by accessing the list and
# dividing the population of China (1350)
# by the population of Romania (21).
# Please print your result.

print(countries[0][2] + countries[2][2])

print('##################################################')
##########################################################


# We defined:

stooges = ['Moe', 'Larry', 'Curly']

# but in some Stooges films, Curly was
# replaced by Shemp.

# Write one line of code that changes
# the value of stooges to be:

# ['Moe','Larry','Shemp']

# but does not create a new List
# object.

stooges[2] = 'Shemp'

print(stooges)

print('##################################################')
##########################################################


# Define a procedure, replace_spy,
# that takes as its input a list of
# three numbers, and modifies the
# value of the third element in the
# input list to be one more than its
# previous value.

spy = [0, 0, 7]


def replace_spy(p):
    p[2] += 1


# In the test below, the first line calls your
# procedure which will change spy, and the
# second checks you have changed it.
# Uncomment the top two lines below.

replace_spy(spy)
print(spy)
# >>> [0,0,8]


print('##################################################')
##########################################################


# Define a procedure, sum_list,
# that takes as its input a
# list of numbers, and returns
# the sum of all the elements in
# the input list.

def sum_list(l):
    result = 0
    for i in l:
        result += i
    return result


print(sum_list([1, 7, 4]))
# >>> 12

print(sum_list([9, 4, 10]))
# >>> 23

print(sum_list([44, 14, 76]))
# >>> 134


print('##################################################')
##########################################################


# Define a procedure, measure_udacity,
# that takes as its input a list of strings,
# and returns a number that is a count
# of the number of elements in the input
# list that start with the uppercase
# letter 'U'.


def measure_udacity(p):
    count = 0
    for i in p:
        if i[0] == 'U':
            count += 1
    return count


print(measure_udacity(['Dave', 'Sebastian', 'Katy']))
# >>> 0

print(measure_udacity(['Umika', 'Umberto']))
# >>> 2


print('##################################################')
##########################################################


# Define a procedure, find_element,
# that takes as its inputs a list
# and a value of any type, and
# returns the index of the first
# element in the input list that
# matches the value.

# If there is no matching element,
# return -1.


def find_element(search, value):
    for i in search:
        if i == value:
            return search.index(value)
    return -1


print(find_element([1, 2, 3], 3))
# >>> 2

print(find_element(['alpha', 'beta'], 'gamma'))
# >>> -1


print('##################################################')
##########################################################


# Define a procedure, find_element,
# using index that takes as its
# inputs a list and a value of any
# type, and returns the index of
# the first element in the input
# list that matches the value.

# If there is no matching element,
# return -1.


def find_element_short(search, value):
    if value in search:
        return search.index(value)
    return -1


print(find_element_short([1, 2, 3], 3))
# >>> 2

print(find_element_short(['alpha', 'beta'], 'gamma'))
# >>> -1


print('##################################################')
##########################################################


# Define a procedure, union,
# that takes as inputs two lists.
# It should modify the first input
# list to be the set union of the two
# lists. You may assume the first list
# is a set, that is, it contains no
# repeated elements.


def union(list1, list2):
    for i in list2:
        if i not in list1:
            list1.append(i)


# To test, uncomment all lines
# below except those beginning with >>>.

a = [1, 2, 3]
b = [2, 4, 6]
union(a, b)
print(a)
# >>> [1,2,3,4,6]
print(b)
# >>> [2,4,6]


print('##################################################')
##########################################################


