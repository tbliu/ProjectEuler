def multiples():
    """returns sum of all multiples of 3 and 5 below 1000"""
    sum = 0
    x = 0
    while x < 1000:
        if x % 3 == 0:
            sum += x 
            x += 1
        elif x % 5 == 0:
            sum += x
            x += 1
        else:
            x += 1
    print(sum)

multiples() 
