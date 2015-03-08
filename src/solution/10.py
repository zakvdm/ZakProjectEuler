knownPrimes = [ 2, 3, 5, 7 ]

limit = 2000000

def isPrime(number):
    for prime in knownPrimes:
        # Early out:
        if prime * prime > number:
            return True
        if number % prime == 0:
            return False

    return True

candidate = 11
count = 0

print(isPrime(1999979))

while candidate < limit:
    if isPrime(candidate):
        knownPrimes.append(candidate)
    if isPrime(candidate + 2):
        knownPrimes.append(candidate + 2)
        
    candidate = candidate + 6

    if count == 10000:
        print("Candidate is: " + str(candidate))
        count = 0

    count = count + 1    

sum = 0
for num in knownPrimes:
    sum = sum + num

print("ANSWER:")
print(knownPrimes[:10])
print(knownPrimes[-5:])
print(len(knownPrimes))
print(sum)
    
