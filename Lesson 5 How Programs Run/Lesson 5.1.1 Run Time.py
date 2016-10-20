# import time
#
#
# def time_execution(code):
#     start = time.clock()
#     result = eval(code)
#     run_time = time.clock() - start
#     return result, run_time
#
#
# def spin_loop(n):
#     i = 0
#     while i < n:
#         i += 1
#
# print(time_execution('spin_loop(10 ** 8)')[1])


import time


def time_execution(function, input):
    start = time.clock()
    result = function(input)
    run_time = time.clock() - start
    return result, run_time


def spin_loop(n):
    i = 0
    while i < n:
        i += 1

for i in range(0, 10):
    print(i, time_execution(spin_loop, 10 ** i)[1])
