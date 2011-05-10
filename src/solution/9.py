def isTriplet(a, b, c):
    return a**2 + b**2 == c**2


for a in range(1, 1000):
    print("a = " + str(a))
    for b in range(a, 1000):
        for c in range(b, 1000):
	    if a + b + c == 1000 and isTriplet(a, b, c):
	         print(str(a) + " " + str(b) + " " + str(c))
             
