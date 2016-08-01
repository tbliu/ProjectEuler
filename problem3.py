def largest_prime(max):
    x = 1
    largest = 0
    while (x < max):
        if max % x == 0:
            if x % 2 != 0 and x % 3 != 0:
                if is_prime(x) == True and x > largest:
                    largest = x
                    print(largest)
        x += 1
    print(largest)
            
            
def is_prime(x):
    if x == 1:
        return True
    else:
        i = 2
        prime = True
        while i < x:
            if x % i == 0:
                prime = False
            i += 1
    return prime


#largest_prime(13195)
largest_prime(600851475143)
