import Helper

class Problem:
    badPairs = {} 
    def nextPrime(self, prime):
        for newPrime in self.sequenceOfPrimes:
            if newPrime > prime:
                return newPrime
        print("RAN OUT OF PRIMES!")
    
    def iterator(self):
        result = [11, 7, 5, 3, 2]
        while True:
            #print(result)
            yield result
            
            result = self.findNextInteration(result)
            
    def findNextInteration(self, result):
        while True:
            if self.nextPrimeDict[result[-1]] < result[-2]:
                result[-1] = self.nextPrimeDict[result[-1]]
            elif self.nextPrimeDict[result[-2]] < result[-3]:
                result[-2] = self.nextPrimeDict[result[-2]]
                result[-1] = 3
            elif self.nextPrimeDict[result[-3]] < result[-4]:
                result[-3] = self.nextPrimeDict[result[-3]]
                result[-2] = 7
                result[-1] = 3
            elif self.nextPrimeDict[result[-4]] < result[-5]:
                result[-4] = self.nextPrimeDict[result[-4]]
                result[-3] = 11
                result[-2] = 7
                result[-1] = 3
            else:
                nextPrime = self.nextPrimeDict[result[0]]
                result = [nextPrime, 13, 11, 7, 3]
            
            if not self.hasBadPair(result):
                return result
    
    def hasBadPair(self, result):
        for i in range(0, 4):
            if self.badPairs.get((result[i], result[i + 1])):
                return True
        return False        
                
    def testPrimeGroup(self, thePrimes):
        if len(thePrimes) == 1:
            return True
        currentPrime = str(thePrimes[0])
        for otherPrime in thePrimes[1:]:
            comb1 = int(currentPrime + str(otherPrime))
            comb2 = int(str(otherPrime) + currentPrime)
            if comb1 > self.maxPrime or comb2 > self.maxPrime:
                print("RAN OUT OF PRIMES!!!!")
                return True
            if not self.primes.get(comb1) or not self.primes.get(comb2):
                self.badPairs[(thePrimes[0], otherPrime)] = True
                return False
        result = self.testPrimeGroup(thePrimes[1:])
        print('NOTE: CHANCE OF FINDING A LONGER BAD GROUPING!')
        if not result:
            print('WOOP, NOW IVE FOUND A BETTER BAD GROUPING!' + str(thePrimes[1:]))
            self.badPairs[tuple(thePrimes[1:])] = True
        return result
            
    def run(self):
        allKeys = Helper.primesLessThan(1000000)
        self.sequenceOfPrimes = [prime for prime in allKeys.keys() if allKeys[prime]]
        self.sequenceOfPrimes.sort()
        self.maxPrime = self.sequenceOfPrimes[-1]
        
        # CACHE ALL THE NEXT PRIMES
        self.nextPrimeDict = {}
        currentPrime = self.sequenceOfPrimes[0]
        while currentPrime < self.maxPrime:
            previousPrime = currentPrime
            currentPrime = self.nextPrime(currentPrime)
            self.nextPrimeDict[previousPrime] = currentPrime
            
            
        print(self.maxPrime)
        self.primes = dict([(prime, True) for prime in allKeys.keys() if allKeys[prime]])
        
        count = 0
        for leftPrime in self.sequenceOfPrimes:
            count = count + 1
            if count % 100 == 0:
                print(count)
            if self.testPrimeGroup([leftPrime, 673, 109, 7, 3]):
                print('IVE DONE IT!')
                print(leftPrime)
                return
            
        
        
        #print(self.sequenceOfPrimes)
        #print(self.primes)
        
        count = 0
        for primeGroup in self.iterator():
            count = count + 1
            result = self.testPrimeGroup(primeGroup)
            if result:
                print('FUCK YEAH!')
                print(primeGroup)
                return
            if count % 100 == 0:
                print('Num of bad keys: ' + str(len(self.badPairs.keys())))
                print(primeGroup)
            
       


if __name__ == '__main__':
    solver = Problem()
    solver.run()