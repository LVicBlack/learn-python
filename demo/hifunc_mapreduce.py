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


# print(str2int('18954'))

# 练习
# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
# 输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
def standard_name_list(name_list):
    def standard_name(name):
        return str.capitalize(name)

    return list(map(standard_name, name_list))


# print(standard_name_list(['adam', 'LISA', 'barT']))


# 编写一个prod()函数，可以接受一个list并利用reduce()求积：
def prod(x, y):
    return x * y


# print(reduce(prod,[3, 5, 7, 9]))


# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456
def str2float(s):
    s_split = str.split(s, '.')

    def char2num(c):
        return DIGITS[c]

    def fn(x, y):
        return 10 * x + y

    def fn_dec(x, y):
        return x / 10 + y

    # 整数部分
    # print(reduce(fn, map(char2num, s_split[0])))
    # 小数部分
    # print(reduce(fn_dec, map(char2num, s_split[1][::-1])))
    return reduce(fn, map(char2num, s_split[0])) + reduce(fn_dec, map(char2num, s_split[1][::-1])) / 10


print(str2float('123.456'))
