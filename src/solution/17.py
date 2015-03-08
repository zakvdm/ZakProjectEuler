basics = { 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine',
           10:'ten', 11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen',
           20:'twenty', 30:'thirty', 40:'forty', 50:'fifty', 60:'sixty', 70:'seventy', 80:'eighty', 90:'ninety' }

def numToWord(x):
    """Convert a number into a word representation:
    >>> [numToWord(n) for n in range(1, 5)]
    ['one', 'two', 'three', 'four']
    >>> numToWord(1000)
    'onethousand'
    >>> numToWord(21)
    'twentyone'
    >>> numToWord(400)
    'fourhundred'
    >>> numToWord(739)
    'sevenhundredandthirtynine'
    """
    if basics.has_key(x):
        return basics[x]

    if x == 1000:
        return 'onethousand'

    word = ''

    hundreds = int(x / 100)
    if hundreds > 0:
        word = word + basics[hundreds] + 'hundred'

    tens = x % 100
    if tens == 0:
        return word
    if hundreds > 0:
        word = word + 'and'
    if basics.has_key(tens):
        return word + basics[tens]
    else:
        ones = tens % 10
        return word + basics[tens - ones] + basics[ones]

def findAnswer():
    sum = 0
    for num in range(1, 1001):
        sum = sum + len(numToWord(num))

    print(sum)

def _test():
    import doctest
    doctest.testmod()

if __name__ == "__main__":
    _test()
    findAnswer()

    
    
