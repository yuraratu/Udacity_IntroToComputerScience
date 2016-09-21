# Investigating adding and appending to lists
# If you run the following four lines of codes, what are list1 and list2?

list1 = [1,2,3,4]
list2 = [1,2,3,4]

list1 = list1 + [5, 6]
list2.append([5, 6])

# to check, you can print them out using the print statements below.

print("showing list1 and list2:")
print(list1)
print(list2)


print('##################################################')
##########################################################


# A list is symmetric if the first row is the same as the first column,
# the second row is the same as the second column and so on. Write a
# procedure, symmetric, which takes a list as input, and returns the
# boolean True if the list is symmetric and False if it is not.


def symmetric(p):
    i = 0
    while i < len(p):
        if len(p) != len(p[i]):
            return False
        j = 0
        while j < len(p[i]):
            if p[i][j] != p[j][i]:
                return False
            j += 1
        i += 1
    return True

print(symmetric([[1, 2, 3],
                [2, 3, 4],
                [3, 4, 1]]))
# >>> True

print(symmetric([["cat", "dog", "fish"],
                ["dog", "dog", "fish"],
                ["fish", "fish", "cat"]]))
# >>> True

print(symmetric([["cat", "dog", "fish"],
                ["dog", "dog", "dog"],
                ["fish","fish","cat"]]))
# >>> False

print(symmetric([[1, 2],
                [2, 1]]))
# >>> True

print(symmetric([[1, 2, 3, 4],
                [2, 3, 4, 5],
                [3, 4, 5, 6]]))
# >>> False

print(symmetric([[1,2,3],
                 [2,3,1]]))
# >>> False

print(symmetric([['cricket', 'football', 'tennis'], ['golf']]))
# >>> False


print('##################################################')
##########################################################


# The mean of a set of numbers is the sum of the numbers divided by the
# number of numbers. Write a procedure, list_mean, which takes a list of numbers
# as its input and return the mean of the numbers in the list.

# Hint: You will need to work out how to make your division into decimal
# division instead of integer division. You get decimal division if any of
# the numbers involved are decimals.


def list_mean(p):
    if len(p) == 0:
        return 'incorrect'
    sum = 0.0
    count = 0
    for i in p:
        sum += i
        count += 1
    return sum / count


print(list_mean([1, 2, 3, 4]))
# >>> 2.5
print(list_mean([1, 3, 4, 5, 2]))
# >>> 3.0
print(list_mean([]))
# >>> ??? You decide. If you decide it should give an error, comment
# out the print line above to prevent your code from being graded as
# incorrect.
print(list_mean([2]))
# >>> 2.0
