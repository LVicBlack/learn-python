# 生成器
## 方法1：对比列表生成式
# L = [x * x for x in range(10)]
# print(L)
# g = (x * x for x in range(10))
# print(g)

# 打印生成器
# 1.使用next(gene)方法，计算出下一个元素的值，直到计算到最后一个元素
# 但是没有更多的元素时，抛出StopIteration的错误。
# print(next(g))
# print(next(g))

# 2.使用for循环遍历
# for element in g:
#     print(element)

## 方法2：yield断点
# # 斐波那契
# def fib(n):
#     cur, a, b = 0, 0, 1
#     while (cur < n):
#         yield b
#         a, b = b, a + b
#         cur = cur + 1
#     return "finish:", b
#
#
# print(fib(6))
# # 获取gene的返回值
# fib = fib(6)
# # for f in fib:
# #     print(f)
# while True:
#     try:
#         x = next(fib)
#         print('fib:', x)
#     except StopIteration as e:
#         print('Generator return value:', e.value)
#         break

# def odd():
#     print('step 1')
#     yield 1
#     print('step 2')
#     yield 3
#     print('step 3')
#     yield 5
#
# for o in odd():
#     print(o)

# 杨辉三角
# 笨拙方法
# def triangles():
#     cur = 1
#     row = [1]
#     while True:
#         yield row
#         if cur == 1:
#             row = [1, 1]
#         else:
#             index = 0
#             newRow = [1]
#             while (index + 1) < cur:
#                 newRow.append(row[index] + row[index + 1])
#                 index = index + 1
#             newRow.append(row[index])
#             row = newRow
#         cur = cur + 1


# zip方法
def triangles():

    out = [1]

    while True:

        yield out

        out = [sum(i) for i in zip([0]+out, out+[0])]

n = 0
results = []
for t in triangles():
    results.append(t)
    n = n + 1
    if n == 10:
        break

for t in results:
    print(t)

if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')