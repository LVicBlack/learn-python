# 迭代
# 判断是否可以迭代
from collections.abc import Iterable

# print(isinstance('abc', Iterable))
# print(isinstance([1, 2, 3], Iterable))
# print(isinstance(123, Iterable))

# map
exMap = {'a': 1, 'b': 2, 'c': 3}


# key
# for key in exMap:
#     print(key)
#
# # value
# for value in exMap.values():
#     print(value)
#
# # k,v
# for k, v in exMap.items():
#     print(k, ' ::: ', v)


# list
# # 下标循环
# exList = ['A', 'B', 'C']
# for i, v in enumerate(exList):
#     print(i, ' ::: ', v)
#
# # 二维数组
# for x, y in [(1, 1), (2, 4), (3, 9)]:
#     print(x, y)


def findMinAndMax(list):
    minValue = None
    maxValue = None
    for v in list:
        if not isinstance(v, (int, float)):
            raise TypeError('请输入数字')
        if minValue is None:
            minValue = v
        elif minValue > v:
            minValue = v
        if maxValue is None:
            maxValue = v
        elif maxValue < v:
            maxValue = v
    return minValue, maxValue


# print(findMinAndMax([(1, 1), (2, 4), (3, 9)]))
# try:
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
# except TypeError as e:
#     print(e)
