def primesLessThan(n):
    """
    >>> primesLessThan(10)
    [1, 2, 3, 5, 7]
    >>> primesLessThan(40)
    [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    """
    candidates = {}
    for i in range(1, n):
        candidates[i] = True
        
    candidates[1] = False
    
    for i in range(2, n):
        if i % 100000 == 0:
            print('.')
        if not candidates[i] == False:
            if isPrime(i):
                # Eliminate multiples:
                k = 2
                while k * i < n:
                    candidates[k*i] = False
                    k = k + 1
    
    #return [k for k in candidates if candidates[k] == True]
    return candidates

def isPrime(n):
    if n <= 0:
        return False
    
    test = 2
    while test**2 <= n:
        if n % test == 0:
            return False
        test = test + 1
    
    return True

def listPermutations(n):
    """
    List all permutations of numbers length n
    """
    if n == 2:
        return ['12', '21']
    
    permutations = []
    for perm in listPermutations(n - 1):
        for i in range(0, len(perm) + 1):
            leftside = perm[:i]
            rightside = perm[len(leftside):]
            permutations.append(leftside + str(n) + rightside)
            
    return permutations

def listPermutationsWithZero(n):
    """
    List all permutations of numbers length n
    """
    if n == 1:
        return ['01', '10']
    
    permutations = []
    for perm in listPermutationsWithZero(n - 1):
        for i in range(0, len(perm) + 1):
            leftside = perm[:i]
            rightside = perm[len(leftside):]
            permutations.append(leftside + str(n) + rightside)
            
    return permutations

def findDivisors(x):
    """
    >>> findDivisors(4)
    [1, 2]
    #>>> findDivisors(220)
    #[1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110]
    #>>> findDivisors(284)
    #[1, 2, 4, 71, 142]
    #>>> findDivisors(28123)
    #[1]
    """
    divisors = []
    candidate = 2
    while candidate ** 2 <= x:
        if x % candidate == 0:
            i = len(divisors) / 2
            divisors.insert(i, candidate)
            if x / candidate != candidate:
                divisors.insert(i + 1, x / candidate)
        candidate = candidate + 1
    divisors.insert(0,1) # 1 is a divisor too!
    return divisors

def sumOfMissingNumbers(numbers):
    """
    >>> sumOfMissingNumbers({3:True, 4:True, 7:True, 10:True})
    31
    """
    maxKey = max(numbers.keys())
    missingNumbers = []
    for i in range(1, maxKey + 1):
        if not numbers.has_key(i):
            missingNumbers.append(i)

    return sum(missingNumbers)

def numberToDigits(number):
    numString = str(number)
    return [numString[x] for x in range(0, len(numString))]

def _test():
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    _test()
