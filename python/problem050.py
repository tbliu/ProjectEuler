import time

start = time.time()

def prime_sum(x):
    primes = {1: 2} # contains all primes under x -- {index: number} (Need index later)
    composite = {} # contains all non primes under x -- {number: index} (Faster)
    i = 3 # primes
    p_index = 2
    c_index = 1
    while i < x:
        k = i
        if i not in composite:
            while (i * k) < x: # Sieves composites of primes (see problem10)
                composite[i * k] = c_index
                k += 1
                c_index += 1
            primes[p_index] = i
            p_index += 1
        i += 2 # Skip every even number

    chains = {} # {chain length: sum of chain}
    tracker = 1 # Keeps track of what index currentlyl on in primes
    while tracker in primes:
        sum = 0
        i = tracker
        chain = 0
        while i in primes:
            if sum + primes[i] > x:
                break
            sum += primes[i]
            chain += 1
            if sum in primes.values(): # if sum is prime, add to chains
                chains[chain] = sum
            i += 1
        tracker += 1
    print(chains[max(chains)], time.time() - start)
    

prime_sum(1000000)
        
# time = 965.1721849441528
