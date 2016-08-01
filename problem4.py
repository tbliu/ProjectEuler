def largest_palindrome():
    first = 100
    second = 100
    largest = 0
    total = first * second
    while (first <= 999):
        while (second <= 999):
            if is_palindrome(total) == True:
                if total > largest:
                    largest = total
            second += 1
            total = first * second
        first += 1
        second = 100
        total = first * second
    print(largest)
        

def is_palindrome(x):
    """
    >>>is_palindrome(2)
    True
    >>>is_palindrome(22)
    True
    >>>is_palindrome(424)
    True
    >>>is_palindrome(599)
    False
    """
    y = str(x)
    y = y[::-1]
    if x == int(y): 
        return True
    return False


largest_palindrome()
