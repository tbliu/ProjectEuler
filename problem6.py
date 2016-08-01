def square_of_sum(x):
    sum = 0
    i = 1
    while i <= x:
        sum += i
        i += 1
    return sum * sum

def sum_of_squares(x):
    sum = 0
    i = 1
    while i <= x:
        sum += i * i
        i += 1
    return sum

def main(n):
    #print(sum_of_squares(n))
    #print(square_of_sum(n))
    print(square_of_sum(n) - sum_of_squares(n))

main(100)