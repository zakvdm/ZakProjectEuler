import helper

def checkAbundant(x):
    """
    >>> checkAbundant(4)
    False
    >>> checkAbundant(12)
    True
    >>> checkAbundant(11)
    False
    >>> checkAbundant(28)
    False
    >>> checkAbundant(28123)
    False
    >>> checkAbundant(88)
    True
    >>> checkAbundant(28035)
    True
    """
    divs = helper.findDivisors(x)
    total = sum(divs)
    return total > x

def findAllAbundants(x):
    """
    >>> findAllAbundants(20)
    [12, 18, 20]
    """
    abundants = []
    for x in range(1, x + 1):
        if checkAbundant(x):
            abundants.append(x)
    return abundants

def findSumsOfAbundants(abundants):
    """
    >>> findSumsOfAbundants([12, 18, 20])
    {32: True, 36: True, 38: True, 40: True, 24: True, 30: True}
    """
    sumOfAbundants = {}
    for i in range(0, len(abundants)):
        lhs = abundants[i]
        for j in range(i, len(abundants)):
            rhs = abundants[j]
            sum = lhs + rhs
            if sum < 28124:
                sumOfAbundants[sum] = True

    return sumOfAbundants
        
    
def findAnswer():
    abundants = findAllAbundants(28123)
    print('Found abundant numbers: ' + str(len(abundants)))
    sumOfAbundants = findSumsOfAbundants(abundants)
    print('Found sums of abundant numbers: ' + str(len(sumOfAbundants)))
    print(max(sumOfAbundants.keys()))

    print(helper.sumOfMissingNumbers(sumOfAbundants))

def _test():
    import doctest
    doctest.testmod()

if __name__ == "__main__":
    _test()
    findAnswer()
