import time

start = time.time()

def sum_power(x):
    """Finds sum of all numbers that can be written as the xth power of their digits"""
    i = 2 # 1^x is not included
    s = set()
    sum = 0
    ### Largest possible number will be 999...9 with each 9 raised to x power ###
    ### Number of 9's has an upperbound of 10^x - 1 (which yields a number of all 9's) ###
    while i < (split_digits(10 ** x - 1, x)):  
        if i == split_digits(i, x):
            s.add(i)
        i += 1
    for value in s:
        sum += value
    print(sum, time.time() - start)
    

def split_digits(num, power):
    """Sums the digits raised to a certain power of a certain number"""
    sum = 0
    while num:
        sum += (num % 10) ** power
        num //= 10
    return sum

sum_power(5)
    