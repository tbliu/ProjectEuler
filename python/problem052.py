import time

start = time.time()

def same_digits(x, y):
    """Checks if two numbers have the same digits regardless of order"""
    x_lst = []
    while x: # appends digits of x to a list
        x_lst.append(x % 10)
        x //= 10
   
    y_lst = [] # appends digits of y to a list
    while y:
        y_lst.append(y % 10)
        y //= 10
    
    if len(x_lst) != len(y_lst): # if lengths of each list are different, lists cannot be equal
        return False
    
    while x_lst != []: 
        if x_lst[0] not in y_lst: # return false if first element in x_lst is not in y_lst
            return False
        else:
            y_lst.remove(x_lst[0]) # else remove first element in each list and continue checking
            x_lst.remove(x_lst[0])
    return x_lst == []

def smallest_int(x):
    """Finds the smallest number n where 2 * n, 3 * n, ... , x * n have the same digits"""
    n = 1
    mult = 2 # start with 2x
    while True:
        if mult == x and same_digits(n, mult * n): 
            print(n, time.time() - start)
            return
        elif same_digits(n, mult * n):
            mult += 1
        else:
            n += 1
            mult = 2

smallest_int(6)
