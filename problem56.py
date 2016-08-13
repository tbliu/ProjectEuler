import time

start = time.time()

def digit_sum(x, y):
    """Calculates maximum digital sum from the number a ** b where a < x and b < y"""
    a = 1
    sums = set()
    nums = set()
    while a < x:
        b = 1
        while b < y:
            if a ** b not in nums:
                sums.add(sum_digits(a ** b))
                nums.add(a ** b)
            b += 1
        a += 1
    print(max(sums), time.time() - start)

def sum_digits(x):
    """Sums the digits of a number"""
    sum = 0
    while x:
        sum += x % 10
        x //= 10
    return sum

digit_sum(100, 100)