# Define a procedure, add_to_index,
# that takes 3 inputs:

# - an index: [[<keyword>,[<url>,...]],...]
# - a keyword: String
# - a url: String

# If the keyword is already
# in the index, add the url
# to the list of urls associated
# with that keyword.

# If the keyword is not in the index,
# add an entry to the index: [keyword,[url]]

index = []


def add_to_index(index, keyword, url):
    for sublist in index:
        if sublist[0] == keyword:
            sublist[1].append(url)
            return
    else:
        index.append([keyword, [url]])


add_to_index(index,'udacity','http://udacity.com')
add_to_index(index,'computing','http://acm.org')
add_to_index(index,'udacity','http://npr.org')
print(index)
# >>> [['udacity', ['http://udacity.com', 'http://npr.org']],
# >>> ['computing', ['http://acm.org']]]


print('##################################################')
##########################################################


# Define a procedure, lookup,
# that takes two inputs:

# - an index
# - keyword

# The procedure should return a list
# of the urls associated
# with the keyword. If the keyword
# is not in the index, the procedure
# should return an empty list.

index = [['udacity', ['http://udacity.com', 'http://npr.org']],
         ['computing', ['http://acm.org']]]


def lookup(index, keyword):
    for sublist in index:
        if sublist[0] == keyword:
            return sublist[1]
    return []


print(lookup(index,'udacity'))
# >>> ['http://udacity.com','http://npr.org']
