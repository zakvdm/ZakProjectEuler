import math
from collections import defaultdict
import Helper

class Problem:

    MAX_D = 1000000

    def calcDistinctPrimes(self, d):
        distinct_primes = set()

        cur = d
        while cur > 1:
            prime = self.primeFactorMap[cur]
            cur = cur / prime
            distinct_primes.add(prime)

        #print("distinct primes for " + str(d) + " are: " + str(distinct_primes))
        return distinct_primes

    def calcPhi(self, d, distinctPrimes):
        phi = d
        for p in distinctPrimes:
            phi = phi * (1 - (1.0 / p))

        return phi

    def run(self):

        self.primeFactorMap = Helper.getPrimeFactorMapLessThan(self.MAX_D + 1)

        count = 0

        for d in range(2, self.MAX_D + 1):
            phi = self.calcPhi(d, self.calcDistinctPrimes(d))
            #print("phi for " + str(d) + " is: " + str(phi))
            count = count + phi

        print(count)




if __name__ == '__main__':
    solver = Problem()
    solver.run()
