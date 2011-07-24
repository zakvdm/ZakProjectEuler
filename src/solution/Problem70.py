import math
from collections import defaultdict
import Helper

class Problem:

    primeFactors = dict()

    def findDistinctPrimeFactors(self, n, primes):
        distinct_primes = set()
        remainder = n
        while remainder > 1:
            #print(remainder)
            if remainder in self.primeFactors:
                #print("Using cache on remainder = " + str(remainder) + " for n = " + str(n))
                distinct_primes = distinct_primes | self.primeFactors[remainder]
                break

            for prime in primes:
                if remainder % prime == 0:
                    remainder = remainder / prime
                    distinct_primes.add(prime)
                    break

        self.primeFactors[n] = distinct_primes
        return distinct_primes
        

    def run(self):
        max = 10000000

        print("Finding initial primes...")
        primes = Helper.getPrimeSetLessThan(max)[0]
        prime_list = list(primes)
        prime_list.sort()

        for prime in prime_list:
            self.primeFactors[prime] = set([prime])

        min_n_over_phi = 1.11
        for n in range(2, max + 1):
            if n % 50000 == 0:
               print("Current n = " + str(n))

            distinctPrimeFactors = self.findDistinctPrimeFactors(n, prime_list)

            phi = n
            for prime in distinctPrimeFactors:
                phi = phi * (1 - (1.0 / prime))
                #print(phi)

            n_over_phi = n / phi

            if n_over_phi < min_n_over_phi:
                a = list(str(int(n)))
                b = list(str(int(phi)))
                a.sort()
                b.sort()
                if a == b:
                    print("Found new min:")
                    print("    n = " + str(n))
                    print("    phi = " + str(phi))
                    print("    n / phi = " + str(n_over_phi))
                    min_n_over_phi = n_over_phi
            


if __name__ == '__main__':
    solver = Problem()
    solver.run()
