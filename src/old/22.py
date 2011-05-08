letterScores = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}

def getNameScore(name):
    """
    >>> getNameScore('COLIN')
    53
    >>> getNameScore('zak')
    38
    >>> getNameScore('beef')
    18
    """
    upperName = name.upper()
    score = 0
    for char in upperName:
        score = score + letterScores[char]

    return score

def getSortedNamesList(filePath):
    """
    >>> getSortedNamesList('names.txt')[837]
    'COLIN'
    """
    namesFile = open(filePath, 'r')
    listOfNames = namesFile.read().split(',')
    listOfNames = [name.strip('\"') for name in listOfNames]
    listOfNames.sort()
    return listOfNames
    
def findAnswer():
    sortedListOfNames = getSortedNamesList('names.txt')
    total = 0
    for name in sortedListOfNames:
        total = total + (getNameScore(name) * (sortedListOfNames.index(name) + 1))

    print(total)

def _test():
    import doctest
    doctest.testmod()

if __name__ == "__main__":
    _test()
    findAnswer()
