def memo(function):
    cache = {}
    def memoized(n):
        if function(n) not in cache:
            cache[n] = function(n)
        return cache[n]
    return memoized

def is_prime(x):
    i = 2
    while i < x:
        if x % i == 0:
            return False
        i += 1
    return True

def prime(x):
    count = 0
    i = 1
    while count <= x:
        print(i)
        if is_prime(i) == True:
            count += 1
        i += 1
    print(i)


memo(prime(10001))

