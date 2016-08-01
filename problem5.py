"""def smallest():
    x = 2521
    ans = False
    while ans != True:
        i = 2
        while i <= 20:
            print(x, i)
            if x % i != 0:
                ans = False
                break
            else:
                ans = True
            i += 1
        x += 1
    print(x) """

def smallest():
    x = 1
    for i in range(2, 21):
        if x % i != 0:
            for j in range(2, 21):
                if (x * j) % i == 0:
                    x *= j
                    break
    print(x)
        

smallest()