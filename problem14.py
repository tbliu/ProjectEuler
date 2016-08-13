import time

start_time = time.time()

def collatz(x):
    """Finds the starting number with the largest Collatz sequence under x"""
    seq = {1: 0, 2: 1} # {starting value: sequence length}
    i = 3
    while i < x:
        len = 0
        current_value = i
        while True:
            if current_value in seq: # if value is in seq, add current length to sequence length of value already in seq
                seq[i] = seq[current_value] + len
                break

            if current_value % 2 == 0:
                current_value //= 2
            else:
                current_value = (3 * current_value) + 1
            len += 1
        i += 1

    ### Finds the largest starting value in sequence ###
    largest_chain = 0
    start = 0
    for element in seq:
        if seq[element] > largest_chain:
            largest_chain = seq[element]
            start = element

    print(start, time.time() - start_time)

collatz(1000000)