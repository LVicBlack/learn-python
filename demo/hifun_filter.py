# 和map()类似，filter()也接收一个函数和一个序列。
# 和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。

def not_empty(s):
    return s and s.strip()


# print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))


# 素数
def arr_start_2():
    num = 2
    while True:
        yield num
        num = num + 1


def is_primes(prime):
    return lambda x: x % prime > 0


def primes():
    arr = arr_start_2()  # 初始序列
    while True:
        prime = next(arr)
        yield prime
        arr = filter(is_primes(prime), arr)


primes_arr = []
for n in primes():
    if n < 10:
        primes_arr.append(n)
    else:
        break


# print(primes_arr)


# 练习
# 回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数：
# 二分法
def is_palindrome(n):
    str_n = str(n)
    half_len_n = len(str_n) // 2
    if half_len_n < 1:
        return True
    else:
        return str_n[:half_len_n] == str_n[::-1][:half_len_n]


# is_palindrome = lambda n: str(n) == str(n)[::-1]


output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101,
                                                  111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')
