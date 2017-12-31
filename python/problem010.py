def sum_primes(x):
    """Sums all prime numbers below x"""
    composite = {}
    primes = {}
    i = 3
    sum = 2
    n = 0 
    z = 0 
    while i < x: 
        k = i
        if i not in composite:
            while (i * k) < x:
                composite[i * k] = n
                k += 1
                n += 1
            primes[i] = z
            sum += i
            z += 1
        i += 2
    print("The sum is:", sum)

sum_primes(2000000)
