def fibonacci():
    max = 4000000
    first = 1
    second = 2
    sum = 0
    while (first < max and second < max):
        if second % 2 == 0:
            sum += second
        first, second = second, first + second
    print(sum)

fibonacci()
