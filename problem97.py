import time

start = time.time()

def non_mersenne():
    """Finds the last 10 digits of a large non-Merseenene prime: 28433×2**7830457+1"""
    lst = []
    prime = 28433 * (2**7830457)+1
    while len(lst) < 10:
        lst.append(prime % 10) # appends last digit to list (will be in reverse order)
        prime //= 10
    lst.reverse()
    print(lst)

non_mersenne()