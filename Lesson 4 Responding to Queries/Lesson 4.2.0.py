# 1 Gold Star

# The built-in <string>.split() procedure works
# okay, but fails to find all the words on a page
# because it only uses whitespace to split the
# string. To do better, we should also use punctuation
# marks to split the page into words.

# Define a procedure, split_string, that takes two
# inputs: the string to split and a string containing
# all of the characters considered separators. The
# procedure should return a list of strings that break
# the source string up by the characters in the
# splitlist.


def split_string(source, splitlist):
    result = []
    at_split = True
    for char in source:
        if char in splitlist:
            at_split = True
        else:
            if at_split:
                result.append(char)
                at_split = False
            else:
                result[-1] = result[-1] + char
    return result


    # result = []
    # to_split = source
    # while len(to_split) > 0:
    #     indexes = []
    #     for i in splitlist:
    #         try:
    #             indexes.append(to_split.index(i))
    #         except:
    #             continue
    #     if len(indexes) > 0 and min(indexes) != 0:
    #         next_position = min(indexes)
    #         result.append(to_split[:next_position])
    #         if next_position + 1 < len(to_split):
    #             to_split = to_split[next_position + 1:]
    #         else:
    #             to_split = ''
    #     elif len(indexes) == 0:
    #         result.append(to_split)
    #         return result
    #     elif min(indexes) == 0:
    #         to_split = to_split[1:]
    #     else:
    #         result.append(to_split)
    # return result


out = split_string("First Name,Last Name,Street Address,City,State,Zip Code", ",")
print(out)
# >>>['First Name', 'Last Name', 'Street Address', 'City', 'State', 'Zip Code']

out = split_string("After  the flood   ...  all the colors came out.", " .")
print(out)
# >>> ['After', 'the', 'flood', 'all', 'the', 'colors', 'came', 'out']

out = split_string("This is a test-of the,string separation-code!", " ,!-")
print(out)
# >>> ['This', 'is', 'a', 'test', 'of', 'the', 'string', 'separation', 'code']
