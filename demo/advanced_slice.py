# 1.数组切片
rangeList = list(range(100))

# # 前10
# print(rangeList[:10])
# # 后10
# print(rangeList[-10:])
# # 10-20.
# print(rangeList[10:20])
# # 所有数，每10个取一个
# print(rangeList[::10])
# # 前10个数，每两个取一个
# print(rangeList[:10:2])
# # 10-20，每两个取一个
# print(rangeList[10:20:2])

# 去除字符串首尾的空格
def trim(s):
    while s[0] == ' ':
        s = s[1:]
    while s[-1] == ' ':
        s = s[:-1]
    print(s)

trim("   222  ")