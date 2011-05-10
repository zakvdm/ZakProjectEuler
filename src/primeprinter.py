import Helper
from collections import defaultdict

def trueFactory():
    return True

def print_primes():
    increment = 35000000
    iterations = 5 
    iteration = 1
    allNumbers = Helper.primesLessThan(increment)

    primes = [num for num in allNumbers if allNumbers[num]]

    # Because of memory constraints, I can't apply the seive all at once, instead I apply it incrementally
    while iteration < iterations:
        # First reset the map to free up the memory
        allNumbers = defaultdict(trueFactory)

        # Now we have to eliminate multiples of all primes found so far from the current range (as if the seive had been applied all along)
        iteration = iteration + 1
        start = (iteration - 1) * increment
        maximum = increment * iteration
        allNumbers[start] = Helper.isPrime(start)
        for prime in primes:
            i = int(start / prime) + 1
            while i * prime < maximum:
                allNumbers[i * prime] = False
                i = i + 1

        # Finally we are ready to continue with the seive as per normal
        for number in range(start, int(maximum / 2) + 1):
            if allNumbers[number]:
                i = 2
                while i * number < maximum:
                    allNumbers[i * number] = False
        # Add these new primes to the ones we already now about, rinse and repeat
        primes = primes + [num for num in range(start, maximum) if allNumbers[num]]

    f = open('./primes','w')
    for prime in primes:
        f.write(str(prime) + "\n")
    f.close()

def read_primes():
    primes_file = open('./primes','r')
    primes = set()
    for prime in primes_file:
        primes.add(prime)

    print(str(len(primes)))
    print("done!")

if __name__ == "__main__":
    print_primes()
    #read_primes()
