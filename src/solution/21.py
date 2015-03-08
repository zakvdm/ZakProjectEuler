def findDivisors(x):
    """
    >>> findDivisors(220)
    [1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110]
    >>> findDivisors(284)
    [1, 2, 4, 71, 142]
    """
    divisors = []
    for div in range (1, int(x / 2) + 1):
        if x % div == 0:
            divisors.append(div)
    return divisors
    
def d(x):
    """
    >>> d(220)
    284
    >>> d(284)
    220
    """
    return sum(findDivisors(x))
    
def isAmicable(x):
    """
    >>> isAmicable(220)
    True
    >>> isAmicable(284)
    True
    >>> isAmicable(3422)
    False
    """
    return d(d(x)) == x


def findAnswer():
    sum = 0
    for num in range(1, 10000):
        if isAmicable(num):
            if d(num) != num:
                print(num)
                sum = sum + num

    print(sum)

def _test():
    import doctest
    doctest.testmod()

if __name__ == "__main__":
    _test()
    findAnswer()
