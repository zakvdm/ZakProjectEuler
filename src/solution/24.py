import math

def swapBackWithDigitAtIndex(chars, swapIndex):
    """
    >>> swapBackWithDigitAtIndex('3423', 2)
    '3432'
    >>> swapBackWithDigitAtIndex('6423', 0)
    '3642'
    >>> swapBackWithDigitAtIndex('021', 0)
    '102'
    """
    swapper = chars[-1]
    out = chars[:-1]
    return out[:swapIndex] + swapper + out[swapIndex:]


def findNextPermutation(x):
    """
    >>> findNextPermutation('012')
    '021'
    >>> findNextPermutation('021')
    '102'
    >>> findNextPermutation('0123456789')
    '0123456798'
    >>> findNextPermutation('132048596')
    '132048659'
    """
    for i in range(1, len(x)):
        swapIndex = (len(x) - 1) - i
        candidate = swapBackWithDigitAtIndex(x, swapIndex)
        if int(candidate, 10) > int(x, 10):
            return candidate
    return -1

def countPermutationsUpTo(chars, foundSoFar, target):
    """
    >>> countPermutationsUpTo('012', 0, 3)
    ('1', 2)
    >>> countPermutationsUpTo('02', 2, 3)
    ('0', 2)
    >>> countPermutationsUpTo('2', 2, 3)
    ('2', 3)
    >>> countPermutationsUpTo('012', 0, 5)
    ('2', 4)
    """
    # Hold chars[0] constant, and count permutations
    if len(chars) == 1:
        return (chars[0], foundSoFar + 1)
    
    count = len(chars)
    permsPerChar = math.factorial(count - 1)
    char = chars[0]
    chars = chars[1:]
    perms = 0
    for i in range(0, count):
        # We want to stop before we overflow the target:
        if perms + permsPerChar + foundSoFar >= target:
            return (char, perms + foundSoFar)

        perms = perms + permsPerChar
        char = chars[0]
        chars = chars[1:]
    

def findNthPermutation(startString, n):
    """
    >>> findNthPermutation('012', 5)
    201
    """
    resultString = ''
    foundSoFar = 0
    remainingChars = startString
    for i in range(0, len(startString)):
        result = countPermutationsUpTo(remainingChars, foundSoFar, n)
        foundSoFar = result[1]
        char = result[0]
        resultString = resultString + char
        remainingChars = remainingChars[:remainingChars.index(char)] + remainingChars[remainingChars.index(char) + 1:]

    print(resultString)
    
def findAnswer():
    import math
    print('perms starting with 0 == 9!')
    count = math.factorial(9)
    print(count)
    print('perms starting with 1 == 9!')
    count = count + math.factorial(9)
    print(count)
    print('perms starting with 2 == 9!')
    count = count + math.factorial(9)
    print(count)

    findNthPermutation('0123456789', 1000000)
    
def _test():
    import doctest
    doctest.testmod()

if __name__ == "__main__":
    _test()
    findAnswer()
