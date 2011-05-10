def sumOfDigits(x):
    """
    >>> sumOfDigits(123)
    6
    >>> sumOfDigits(1900)
    10
    >>> sumOfDigits(2342341204324)
    34
    """
    return sum([int(char) for char in str(x)])

def factorial(x):
    """
    >>> factorial(3)
    6
    >>> factorial(5)
    120
    """
    if x == 1:
        return 1
    return x * factorial(x - 1)

def findAnswer():
    num = factorial(100)
    print(num)
    print(sumOfDigits(num))

def _test():
    import doctest
    doctest.testmod()

if __name__ == "__main__":
    _test()
    findAnswer()
