# 函数作为返回值
# 高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回。

# 闭包
### 返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i

        fs.append(f)
    return fs


# print(count()[0]())
# # 元组拆封
# f1, f2, f3 = count()
# f4 = count()
# print(f1())
# print(f2())
# print(f3())
# print(f4[0]())


def counts():
    def f(j):
        def g():
            return j * j

        return g

    fs = []
    for i in range(1, 4):
        fs.append(f(i))
    return fs


# # 元组拆封
# f1, f2, f3 = counts()
# f4 = counts()
# print(f1())
# print(f2())
# print(f3())
# print(f4[0]())


# 练习
# 利用闭包返回一个计数器函数，每次调用它返回递增整数
def createCounter():
    def num_gene():
        num = 0
        while True:
            num = num + 1
            yield num

    n = num_gene()

    def counter():
        return next(n)

    return counter


# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA())  # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')
