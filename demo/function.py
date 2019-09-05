import math


def quadratic(a, b, c):
    conditions = b * b - 4 * a * c
    if conditions > 0 and a != 0:
        answer1 = (-b + math.sqrt(conditions)) / 2 * a
        answer2 = (-b - math.sqrt(conditions)) / 2 * a
        return answer1, answer2
    else:
        return "方程无解"


if quadratic(2, 3, 1) == (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')


# 方法添加默认参数
# 注意：必选参数在前，默认参数在后
# 默认参数必须指向不变对象！
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


# 可变参数 调用该函数时，可以传入任意个参数，包括0个参数
# 在函数内部，参数numbers接收到的是一个tuple
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


nums = [1, 2, 3]
print(calc(nums[0], nums[1], nums[2]))
print(calc(*nums))


# 关键字参数
# **extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict
# kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, city=extra['city'], job=extra['job'])
person('Jack', 24, **extra)


# 命名关键字参数
# 只接收city和job作为关键字参数。这种方式定义的函数如下：
def person(name, age, *, city, job):
    print(name, age, city, job)


person('Jack', 24, city='Beijing', job='Engineer')


# 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了：
def person(name, age, *args, city, job):
    print(name, age, args, city, job)


person('Jack', 24, 1, 2, 3, city='Beijing', job='Engineer')


# 命名关键字参数可以有缺省值，从而简化调用：
def person(name, age, *args, city='city', job):
    print(name, age, args, city, job)


person('Jack', 24, 1, 2, 3, job='Engineer')


# 参数组合顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。

def product(*nums):
    if len(nums)==0:
        raise TypeError('bad operand type,need aless one')
    result = 1
    for num in nums:
        result = result * num
    return result


# print('product() =', product())
print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('测试失败!')
elif product(5, 6) != 30:
    print('测试失败!')
elif product(5, 6, 7) != 210:
    print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        product()
        print('测试失败!')
    except TypeError:
        print('测试成功!')
