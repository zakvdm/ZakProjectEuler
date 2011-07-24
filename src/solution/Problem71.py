import math
from collections import defaultdict
import Helper

class Problem:

    def findNearestFraction(self, denominator):
        numerator = int(denominator / 2) + 1
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


    def run(self):
        print(self.isReducedProperFraction(2, 5))
        d = 1000000
        best_gap_to_3_over_7 = 1

        while d > 2:
            if d % 1000 == 0:
                print("d = " + str(d))
            n = self.findNearestFraction(d)
            if ((3 / 7) - (n / d)) < best_gap_to_3_over_7:
                best_gap_to_3_over_7 = ((3 / 7) - (n / d))
                print("New closest fraction: " + str(n) + "/" + str(d))
            d = d - 1


if __name__ == '__main__':
    solver = Problem()
    solver.run()
