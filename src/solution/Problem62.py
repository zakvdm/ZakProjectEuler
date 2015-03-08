import math
from collections import defaultdict

class Problem:
    def findKey(self, cube):
        keyList = []
        n = 10
        while cube > 0:
            val = cube % n
            keyList.append(cube % n)
            cube = cube - val
            cube = int(cube / n)
        keyList.sort()
        return tuple(keyList)

    def run(self):
        counts = {}

        n = 300
        while True:
            n = n + 1
            cube = n*n*n
            key = self.findKey(cube)
            if not key in counts:
                counts[key] = []
            counts[key].append(cube) 
            
            if len(counts[key]) == 5:
                print(counts[key])
                return


if __name__ == '__main__':
    solver = Problem()
    solver.run()
