import math
from collections import defaultdict
import Helper
import sys

class Problem:

    def countBetween(self, left, right, maxD):
        new = left + right
        
        if new > maxD:
            return 0

        return 1 + self.countBetween(left, new, maxD) + self.countBetween(new, right, maxD)

    def run(self):

        sys.setrecursionlimit(100000)

        print(self.countBetween(3, 2, 12000))


if __name__ == '__main__':
    solver = Problem()
    solver.run()
