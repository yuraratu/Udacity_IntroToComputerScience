# Define a faster fibonacci procedure that will enable us to computer
# fibonacci(36).


def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        last = 1
        before_last = 0
        i = 2
        while i <= n:
            before_last, last = last, last + before_last
            i += 1
    return last

# def fibonacci(n):
#     current = 0
#     after = 1
#     for i in range(0, n):
#         current, after = after, current + after
#     return current


print(fibonacci(36))
# >>> 14930352


# import time
#
# start = time.clock()
#
# for i in range(0, 250):
#     print(int(time.clock() - start), i, fibonacci(i))


mass_of_earth = 5.9722 * 10 ** 24
mass_of_rabbit = 2

n = 1
while fibonacci(n) * mass_of_rabbit < mass_of_earth:
    n += 1
print(n, fibonacci(n))
