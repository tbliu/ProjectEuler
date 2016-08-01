def smallest():
"""Finds smallest number that can be evenly divided by all the numbers from 1 - 20"""
    x = 1
    for i in range(2, 21):
        if x % i != 0:
            for j in range(2, 21):
                if (x * j) % i == 0:
                    x *= j
                    break
    print(x)
        

smallest()
