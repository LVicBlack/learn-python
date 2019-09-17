# 排序算法
# 1
# print(sorted([36, 5, -12, 9, -21]))
#
# # 2
# print(sorted([36, 5, -12, 9, -21], key=abs))
#
# # 3
# print(sorted([36, 5, -12, 9, -21], key=abs, reverse=True))


# 练习
# 用sorted()对上述列表分别按名字排序：
# 一组tuple表示学生名字和成绩：
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def by_name(t):
    return t[0]


L_sorted = sorted(L, key=by_name)
print(L_sorted)
