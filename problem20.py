def fact(n):
    """Computes the sum of digits of the result from calling the factorial of n"""
    sum = 0
    prod = 1
    while n > 0:
        prod *= n
        n -= 1
    while prod > 0:
        sum += prod % 10
        prod //= 10
    print(sum)

fact(100)