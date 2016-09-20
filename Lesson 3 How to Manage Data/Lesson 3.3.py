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
    result = []
    line = []
    i = 0
    while i < len(p):
        for j in p:
            line.append(j[i])
        result.append(line)
        line = []
        i += 1
    return result == p

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