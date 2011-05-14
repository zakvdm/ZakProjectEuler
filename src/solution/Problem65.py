import math
from collections import defaultdict

# 65
# What is most surprising is that the important mathematical constant,
# e = [2; 1,2,1, 1,4,1, 1,6,1 , ... , 1,2k,1, ...].
# 
# The first ten terms in the sequence of convergents for e are:
#       2, 3, 8/3, 11/4, 19/7, 87/32, 106/39, 193/71, 1264/465, 1457/536, ...
class Problem:
    def reduce(self, continuedFraction):
        print("Reducing continued fraction with " + str(len(continuedFraction)) + " terms")
        lastTerm = continuedFraction.pop()
        lastNumerator = 1

        numerator = 0
        denominator = 0

        while len(continuedFraction) > 0:
            # Find common denominator of last 2 components, and divide by 1 (flip fraction)
            term = continuedFraction.pop()
            numerator = (term * lastTerm) + lastNumerator
            denominator = lastTerm
            lastTerm = numerator
            lastNumerator = denominator

        print("Numerator: " + str(numerator))
        print("Denominator: " + str(denominator))

        num_string = str(numerator)
        answer = 0
        for num in num_string:
            answer = answer + int(num)

        print("Numerator sum = " + str(answer))

    def run(self):
        self.reduce([2,1,2,1, 1,4,1, 1,6,1])

        i = 0
        n = 4
        terms = [2, 1, 2]
        while len(terms) < 100:
            if i == 2:
                i = 0
                terms.append(n)
                n = n + 2
            terms.append(1)
            i = i + 1

        self.reduce(terms[:10])
        self.reduce(terms)

    def reduce2(self, reduction, target):
        while True:
            fraction = reduction[-1]
            numerator = fraction[0]
            denom_root = fraction[1]
            denom_int = fraction[2]
            #print("starting fraction: " + str(numerator) + " / root(" + str(denom_root) + ") - " + str(denom_int))
            # So we have a fraction of the form: x / (root(y) + z)
            # and we want to multiply by: (root(y) - z) / (root(y) - z)
            new_num_root = denom_root
            new_num_int = denom_int
            new_denom = denom_root - (denom_int**2)
            # Now we have x(root(y) + z) / y - z**2
            # And we try to eliminate a common denominator
            new_num, new_denom = self.reduceFraction(numerator, new_denom)
            #print("cross multiplied fraction: " + str(new_num) + " * (root(" + str(new_num_root) + ") + " + str(new_num_int) + ") / " + str(new_denom))

            # Now we want to extract a number as close to "target" as possible (but smaller)
            left = 0
            while left + new_denom - new_num_int <= target:
                left = left + new_denom
            y = left - new_num_int
            x = int(left / new_denom)
            # Note: we go from: ((root(a) + b) / c)  ==  x + ((root(a) - y) / c)
            #print("new fraction: " + str(x) + " + ((root(" + str(new_num_root) + ") - " + str(y) + ") / " + str(new_denom) + ")")

            reduction[2].append(x)
            if (new_num_int / new_denom) == target:
                if reduction[2].count(reduction[2][-1]) > 1:
                    print(reduction)

                if not len(reduction[2]) % 2 == 0:
                    self.oddPeriods = self.oddPeriods + 1
                return
            reduction[-1] = (new_denom, new_num_root, y)



    def reduceFraction(self, numerator, denominator):
        #print("Reducing: " + str(numerator) + " / " + str(denominator))
        for i in range(2, min(numerator, denominator) + 1):
            while numerator % i == 0 and denominator % i == 0:
                numerator = numerator / i
                denominator = denominator / i
        #print("To: " + str(numerator) + " / " + str(denominator))
        return int(numerator), int(denominator)


if __name__ == '__main__':
    solver = Problem()
    solver.run()
