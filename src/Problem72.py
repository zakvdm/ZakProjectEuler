import math
from collections import defaultdict
import Helper

class Problem:

    def findNearestFraction(self, denominator):
        numerator = int((3 * denominator) / 7) + 1
        while numerator > 0:
            if (numerator / denominator) < (3 / 7):
                if self.isReducedProperFraction(numerator, denominator):
                    return numerator
            numerator = numerator - 1
        return 0

            
    def isReducedProperFraction(self, numerator, denominator):
        # NOTE: This is SLOOOOOWWWW (could be sped up by pre-caching all the prime factors of numbers and then checking for common primes instead?)
        return self.getGreatestCommonDivisor(numerator, denominator) == 1


    def getGreatestCommonDivisor(self, a, b):
        if a == 0:
            return b
        if b == 0:
            return a
        if a == b:
            return a

        if a > b:
            big = a
            small = b
        else:
            big = b
            small = a

        remainder = big - (int(big / small) * small)

        return self.getGreatestCommonDivisor(remainder, small)

    def eliminateCandidates(self, n, d, eliminatedCandidates):
        multiplier = 2
        den = d * multiplier
        num = n * multiplier
        while den <= self.MAX_D:
            if not den in eliminatedCandidates:
                eliminatedCandidates[den] = set()
            eliminatedCandidates[den].add(num)
            multiplier = multiplier + 1
            den = d * multiplier
            num = n * multiplier


    def countReducedProperFractionsOld(self, d, eliminatedCandidates):
        # NOTE: The reduced fractions are symmetrical around 1 / 2 (eg. 1/8 3/8 | 5/8 7/8)
        #       So we only need to count half and then double
        count = 0  # We always count 1 / d

        n = 1
        while n < d / 2.0:
            if d in eliminatedCandidates and n in eliminatedCandidates[d]:
                n = n + 1
                continue
            #print("FOUND: " + str(n) + "/" + str(d))
            count = count + 1
            self.eliminateCandidates(n, d, eliminatedCandidates)
            n = n + 1

        eliminatedCandidates.pop(d, False)
        print(eliminatedCandidates)
        return count * 2

    primeFactorMap = {}
    primeFactorSets = {}

    def getPrimeFactors(self, num):
        if not num in self.primeFactorSets:
            self.primeFactorSets[num] = Helper.getPrimeFactors(num, self.primeFactorMap)
        return self.primeFactorSets[num]

    def isReducedProperFraction(self, n, d):
        dPrimeFactors = self.getPrimeFactors(d)
        nPrimeFactors = self.getPrimeFactors(n)

        return len(nPrimeFactors & dPrimeFactors) == 0


    def countReducedProperFractions2(self, d):
        # NOTE: The reduced fractions are symmetrical around 1 / 2 (eg. 1/8 3/8 | 5/8 7/8)
        #       So we only need to count half and then double
        #print("FOUND: " + "1/" + str(d))
        count = 1
        #if not d in self.primeFactorSets:
            #self.primeFactorSets[d] = Helper.getPrimeFactors(d, self.primeFactorMap)
        #dPrimeFactors = self.primeFactorSets[d]

        if d % 2 == 0: # EVEN
            n = 3
            while n < d / 2:
                if not self.isReducedProperFraction(n, d):
                    n = n + 1
                    continue
                #print("FOUND: " + str(n) + "/" + str(d))
                count = count + 1
                n = n + 2
        else: # ODD
            if d != 3:
                count = count + 1 # 2 / d is always a RPF
                n = 3
                while n < d / 2.0:
                    #print("FOUND: " + "2/" + str(d))
                    if not self.isReducedProperFraction(n, d):
                        n = n + 1
                        continue # They must have a common factor for this to be true
                    #if not n in self.primeFactorSets:
                        #self.primeFactorSets[n] = Helper.getPrimeFactors(n, self.primeFactorMap)
                    #nPrimeFactors = self.primeFactorSets[n]
                    #print("FOUND: " + str(n) + "/" + str(d))
                    count = count + 1
                    n = n + 1

                    #if (len(nPrimeFactors & dPrimeFactors) == 0):
                        #print(str(n) + "/" + str(d))
                        #count = count + 1

        #print("Count for " + str(d) + " is: " + str(count * 2))

        return count * 2

    def countReducedProperFractions(self, d):
        # NOTE: The reduced fractions are symmetrical around 1 / 2 (eg. 1/8 3/8 | 5/8 7/8)
        #       So we only need to count half and then double
        #print("FOUND: " + "1/" + str(d))
        count = 1
        #if not d in self.primeFactorSets:
            #self.primeFactorSets[d] = Helper.getPrimeFactors(d, self.primeFactorMap)
        #dPrimeFactors = self.primeFactorSets[d]

        n = 2
        while (float(n) / d) < self.PIVOT_POINT:
            #print("TRYING: " + str(n) + "/" + str(d))
            if self.isReducedProperFraction(n, d):
                #print("FOUND: " + str(n) + "/" + str(d))
                count = count + 1
            n = n + 1

        return count

    MAX_D = 1000000

    PIVOT = 1310
    ABOVE_PIVOT_COUNT = 10307
    #PIVOT = 3
    #ABOVE_PIVOT_COUNT = 3
    PIVOT_POINT = 1.0 / PIVOT

    def run(self):
        print("PIVOT POINT: " + str(self.PIVOT_POINT))
        self.primeFactorMap = Helper.getPrimeFactorMapLessThan(self.MAX_D + 1)

        #eliminatedCandidates = {}
        #for i in range(3, MAX_D + 1):
            #n = 1
            #cands = set()
            #while n < i / 2.0:
                #cands.add(n)
                #n = n + 1
            #eliminatedCandidates[i] = cands
        #self.eliminateCandidates(1, 2, eliminatedCandidates)

        print("Counting Reduced Proper Fractions")


        d = self.PIVOT
        count = 0
        while d < self.MAX_D:
            if d % 1000 == 0:
                print("d = " + str(d))
            d = d + 1
            #count1 = self.countReducedProperFractions(d)
            #count2 = self.countReducedProperFractions2(d)
            #if count1 * self.PIVOT != count2:
                #print("############# " + str(d) + " got " + str(count1 * self.PIVOT) + " but should be " + str(count2))
            count = count + self.countReducedProperFractions(d)
        
        print("Answer: " + str((count * self.PIVOT) + self.ABOVE_PIVOT_COUNT))
        return





if __name__ == '__main__':
    solver = Problem()
    solver.run()
