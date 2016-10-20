# Define a procedure, fibonacci, that takes a natural number as its input, and
# returns the value of that fibonacci number.

# Two Base Cases:
#    fibonacci(0) => 0
#    fibonacci(1) => 1

# Recursive Case:
#    n > 1 : fibonacci(n) => fibonacci(n-1) + fibonacci(n-2)


def fibonacci(n):
    if n == 1 or n == 0:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# print(fibonacci(0))
# # >>> 0
# print(fibonacci(1))
# # >>> 1
# print(fibonacci(10))
# # >>> 610

import time

start = time.clock()

for i in range(0, 39):
    print(int(time.clock() - start), i, fibonacci(i))
