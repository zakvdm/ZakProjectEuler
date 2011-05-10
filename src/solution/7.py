knownPrimes = [ 2 ]

def isPrime(number):
    for prime in knownPrimes:
        if number % prime == 0:
            return False

    knownPrimes.append(number)
    return True

primesFound = 1
candidate = 3

while primesFound != 10001:
    if isPrime(candidate):
        primesFound = primesFound + 1

    candidate = candidate + 2

print(knownPrimes[-1])
    
