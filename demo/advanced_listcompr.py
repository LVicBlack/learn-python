# 列表生成式
# 生成[1x1, 2x2, 3x3, ..., 10x10]
import os

indexList = [x * x for x in list(range(1, 11))]
# print(indexList)

# for循环后面还可以加上if判断
indexList = [x * x for x in list(range(1, 11)) if x % 2 == 0]
# print(indexList)

# 多层循环
allList = [m + n for m in 'ABC' for n in 'XYZ']
# print(allList)

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s, str)]
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')