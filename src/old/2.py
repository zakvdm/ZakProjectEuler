def isPalindrome(number):
    numbString = str(number)
    x = 0
    radius = int(len(numbString) / 2)
    for x in range(0, radius):
        if numbString[x] != numbString[len(numbString) - (1 + x)]:
            return False
        
    return True

def findPalindrome(maxNum):
    biggest = 0
    testRange = 100

    for x in range(0, testRange):
        leftSide = maxNum - x
        for y in range(0, testRange):
            rightSide = maxNum - y
            candidate = leftSide * rightSide
            if isPalindrome(candidate):
                if candidate > biggest:
                    biggest = candidate
                    print('current biggest palindrome: ' + str(biggest))

    return biggest

print(findPalindrome(999))

