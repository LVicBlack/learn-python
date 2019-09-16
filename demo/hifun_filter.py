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
print(primes_arr)
