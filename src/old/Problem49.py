import Helper
import math

class Problem49:
    def isPermutation(self, n1, n2):
        n1 = str(n1)
        n2 = str(n2)
        for ch in n1:
            if n1.count(ch) != n2.count(ch):
                return False
        
        return True
            
    
    def run(self):
        print(self.isPermutation(1487, 4817))
        print(self.isPermutation(1487, 8147))
        # cache all 4-digit primes
        primes = []
        print('Caching primes...')
        for i in range(1000, 10000):
            if Helper.isPrime(i):
                primes.append(i)
        quickPrime = set(primes)
        
        print('Looking for suitable primes...')
        # loop over 4-digit primes P
        for i in range(0, len(primes)):
            p1 = primes[i]
            # loop over 4-digit primes P2 > P such that P + P2 < 10000
            for p2 in primes[i + 1:]:
                if p2 + p1 > 10000:
                    break
                
                if not self.isPermutation(p1, p2):
                    continue
                
                
                p3 = p2 + (p2 - p1)
                
                if p1 == 1487 and p2 == 4817:
                    print(self.isPermutation(p1, p3))

                if p3 > 10000:
                    break
                
                # Check if P2 - P is prime
                if p3 in quickPrime and self.isPermutation(p1, p3):
                    print('Yay!')
                    print(p1)
                    print(p2)
                    print(p3)
                    print(str(p1) + str(p2) + str(p3))


if __name__ == '__main__':
    solver = Problem49()
    solver.run()