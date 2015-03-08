def nextNumberInSequence(x):
    if x % 2 == 0:
        return x / 2
    return 3 * x + 1

cache = {}
scope = 1000000
for i in range(1, scope):
    cache[i] = 0

cache[1] = 1

def findValuesForNumber(x):
    if x >= scope:
        return 1 + findValuesForNumber(nextNumberInSequence(x))
    else:
        if cache[x] == 0:
            #print('X is: ' + str(x))
            cache[x] = 1 + findValuesForNumber(nextNumberInSequence(x))

    #print('Returning: ' + str(cache[x]))
    return cache[x]

for val in range(2, scope):
    findValuesForNumber(val)
    if val % (scope / 100) == 0:
        print('Percent complete: ' + str((float(val) / scope) * 100))

max = 0
candidate = 1
for val in range(1, scope):
    if cache[val] > max:
        max = cache[val]
        candidate = val
    
#print(cache)
print(candidate)
