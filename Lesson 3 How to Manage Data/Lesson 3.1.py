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


