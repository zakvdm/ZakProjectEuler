import Helper
import math

class Problem51:
    MAX_NUMBER_OF_DIGITS_TO_REPLACE = 3
    def findPerms(self, prime):
        return [perm for perm in self._findPerms(prime)[1:-1] if perm.count('x') <= self.MAX_NUMBER_OF_DIGITS_TO_REPLACE and perm.count('x') > 0]
    def _findPerms(self, prime):
        prime = str(prime)
        if len(prime) == 2:
            return [prime, 'x' + prime[1], prime[0] + 'x', 'xx']
        
        tmp = []
        for perm in self._findPerms(prime[1:]):
            tmp.append(prime[0] + perm)
            tmp.append('x' + perm)
        
        return tmp
    
    def findPrimeFamily(self, prime, primesDict):
        perms = self.findPerms(prime)
        maxFamily = 0
        bestPerm = ''
        for perm in perms:
            family = 0
            start = 0
            while perm[start] == 'x':
                start = start + 1
            for i in range(start, 10):
                x = int(perm.replace('x', str(i)))
                if primesDict[x]:
                    family = family + 1
            if family > maxFamily:
                bestPerm = perm
            maxFamily = max(maxFamily, family)
        if maxFamily > 7:
            print(bestPerm)
        return maxFamily
                    
        
    def run(self):
        MAX = 1000000
        print(self.findPerms(5603))
        
        print('Caching primes...')
        primesDict = Helper.primesLessThan(MAX);
        maxFamily = 6
        primes = [p for p in primesDict.keys() if primesDict[p] and p > 56003]

        print('Starting search of ' + str(len(primes)) + ' primes...')
        count = 0
        for prime in primes:
            if len(str(prime)) < 3:
                continue
            count = count + 1
            if count % 1000 == 0:
                print('Processing Prime number: ' + str(count))
            family = self.findPrimeFamily(prime, primesDict)
            if family > maxFamily:
                print(family)
                print(prime)
                maxFamily = family


if __name__ == '__main__':
    solver = Problem51()
    solver.run()