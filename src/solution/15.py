cache = {}
width = 20
height = 20

def zeroCache():
    for x in range(0, height + 1):
        for y in range(0, width + 1):
            cache[(x, y)] = 0
            
    cache[(width, height - 1)] = 1
    cache[(width - 1, height)] = 1


def findRoutes(x, y):
    """
    (0, 0) is the top left of the grid. (width, height) is the bottom right.
    """
    if cache[(x, y)] > 0:
        return cache[(x, y)]

    if x == width:
        numRightRoutes = 0
    else:
        numRightRoutes = findRoutes(x + 1, y)

    if y == height:
        numDownRoutes = 0
    else:
        numDownRoutes = findRoutes(x, y + 1)
        
    cache[(x, y)] = numRightRoutes + numDownRoutes
    return cache[(x, y)]

zeroCache()
print(findRoutes(0, 0))

#print(cache)
