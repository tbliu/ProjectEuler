def fib(x):
    """Computes the index of the first number in the fibonnaci sequence to have x number of digits"""
    first = 1
    second = 1
    i = 2 
    while True:
        if num_digits(second) < x:
            second, first = first + second, second
            i += 1
        else:
            break
    print(i)
            

def num_digits(x):
    num = 0
    while x > 0:
        x //= 10
        num += 1
    return num

fib(1000)
