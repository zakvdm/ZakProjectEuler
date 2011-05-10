import Helper
import sys

class Problem:
    bigPrimes = {}
    def nextPrime(self, prime):
        for newPrime in self.sequenceOfPrimes:
            if newPrime > prime:
                return newPrime
        print("RAN OUT OF PRIMES!")

    def isPrime(self, n):
        if n < self.maxPrime:
            return n in self.primes
        if not n in self.bigPrimes:
            self.bigPrimes[n] = Helper.isPrime(n)
        return self.bigPrimes[n]    
 
    def isPrimePair(self, left, right):
        comb1 = int(str(left) + str(right))
        comb2 = int(str(right) + str(left))
        return self.isPrime(comb1) and self.isPrime(comb2)

    def calculateGoodPrimePairs(self):
        maxLeftPrime = 9999
        maxRightPrime = 9999
        index = 0
        primePairs = []
        leftPrime = 3
        while leftPrime < maxLeftPrime:
            if leftPrime % 1000 == 0:
                print("Found good pairs up to left prime: " + str(leftPrime))
                print("So far we've checked " + str(len(self.bigPrimes)) + " overflowing numbers for primality")
            rightPrime = self.nextPrime(leftPrime)
            while rightPrime < maxRightPrime:
                if self.isPrimePair(leftPrime, rightPrime):
                    primePairs.append([leftPrime, rightPrime])
                rightPrime = self.nextPrime(rightPrime)
            leftPrime = self.nextPrime(leftPrime)
        return primePairs

    def expandSets(self, primeSets, primePairs):
        expandedPrimeSets = []
        for primeSet in primeSets:
            for primePair in primePairs:
                if primeSet[-1] == primePair[0]:
                    validExpansion = True
                    for prime in primeSet[:-1]:
                        if not self.isPrimePair(prime, primePair[1]):
                            validExpansion = False
                            continue
                    if validExpansion:
                        expandedPrimeSets.append(primeSet + [primePair[1]])
        return expandedPrimeSets

    def run(self):
        # Get a sequence of primes and a map for easy prime checking
        print("####")
        self.primes, self.maxPrime  = Helper.getPrimeSetLessThan(100000000)
        print("####")
        print(str(len(self.primes)))
        print(str(self.maxPrime))
        self.sequenceOfPrimes = [prime for prime in self.primes]
        self.sequenceOfPrimes.sort()
        
        print("####")
        primePairs = self.calculateGoodPrimePairs()
        print("calculated pairs...")
        primeTriplets = self.expandSets(primePairs, primePairs)
        print("calculated triplets...")
        primeQuadruplets = self.expandSets(primeTriplets, primePairs)
        print("calculated quadruplets...")
        primeFives = self.expandSets(primeQuadruplets, primePairs)
        print("calculated fives...")
        print("####")
        print(primeFives)


if __name__ == '__main__':
    solver = Problem()
    solver.run()
