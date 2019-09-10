# map()函数接收两个参数，一个是函数，一个是Iterable，
# map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
from functools import reduce

# def f(x):
#     return x * x
#
#
# r = map(f, list(range(5)))
#  print(list(r))

# reduce
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def str2int(str):
    def char2num(c):
        return DIGITS[c]

    def fn(x, y):
        return 10 * x + y

    return reduce(fn, map(char2num, str))


print(str2int('18954'))
