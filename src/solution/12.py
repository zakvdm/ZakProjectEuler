import math

triangleNumbers = [ 1, 3, 6 ]

def findTriangleNumbersUpTo(x):
    while len(triangleNumbers) < x:
        triangleNumbers.append(triangleNumbers[-1] + len(triangleNumbers) + 1)
        if len(triangleNumbers) % 1000000 == 0:
            print('Found triangle numbers up to: ' + str(len(triangleNumbers)))

def findTriangleNumber(x):
    number = 0
    i = 0
    while i < x:
        i = i + 1
        number = number + i
        if i % 1000000 == 0:
            print('Found numbers up to: ' + str(i))
 
    return number

def countDivisors(x):
    y = 1
    count = 0
    end = int(math.sqrt(x))
    print(end)

    while y <= end:
        if x % y == 0:
            count = count + 2
            if count % 100 == 0:
                print('Found so far: ' + str(count))
        y = y + 1

    return count
 
#findTriangleNumbersUpTo(20000000)
findTriangleNumbersUpTo(1000000)

print(triangleNumbers[-1])

index = 0
for triangleNum in triangleNumbers:
    print(triangleNum)
    if countDivisors(triangleNum) > 500:
        print(triangleNum)
        break
    index = index + 1

