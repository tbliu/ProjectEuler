def chain(x):
    """Finds number of starting numbers under x which arrive at 89 by summing squares of 
    each digit in a number"""
    values89 = {89: 89} # list of numbers that lead to 89
    values1 = {1: 1} # list of numbers that lead to 1
    i = 2
    j = i
    count = 0
    while i < x:
        if j in values1:  
            j = i
            while j not in values1: # appends values that lead to 1 derived from starting point j
                values1[j] = 1
                j = sum_digits(j)
            i += 1
            j = i
        elif j in values89:
            j = i
            while j not in values89: # appends values that lead to 89 derived from starting point j
                values89[j] = 89
                j = sum_digits(j)
            i += 1
            j = i
            count += 1
        else:
            j = sum_digits(j) # if j not in values89 or values1, continue evaluating sum of its digits
    print(count)
    
def sum_digits(x):
    """Sums the squares of each digit in a number"""
    sum = 0
    while x:
        sum, x = sum + (x % 10) ** 2, x // 10
    return sum

chain(10000000)
