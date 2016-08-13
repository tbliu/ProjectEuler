def prime(n):
"""Finds the 10,001st prime number"""
    primes = [2]
    x = 3
    while True:
        is_prime = True
        for y in primes:
            if x % y == 0:
                is_prime = False  
        if is_prime:
            primes.append(x)
        if len(primes) == n:
            print(primes[n-1])
            return
        x += 2 #skips even numbers


prime(10001)

