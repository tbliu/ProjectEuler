import math
from functools import reduce
import time

start = time.time()

def triplet(x):
    """Finds the product of each value of the pythagorean triplet in which a + b + c = x."""
    trip = {} # {index: [a, b, c]}
    a = 1
    c = 0
    i = 0
    ### Finds all pythagorean triplets under x ###
    while a <= x:
        k = 1
        b = 1
        while b <= x:
            if is_square(a ** 2 + b ** 2):
                c = int(math.sqrt(a ** 2 + b ** 2))
                trip[i] = [a, b, c]
                i += 1
            b += 1
        a += 1
    ### Sums triples ###
    ans = 0
    for element in trip.values():
        if sum(element) == x:
            ans = reduce(lambda d, e: d * e, element)
            break
    print(ans, time.time() - start)

def is_square(x):
    """Determines whether x is a square or not"""
    return int(math.sqrt(x)) == math.sqrt(x)



triplet(1000)