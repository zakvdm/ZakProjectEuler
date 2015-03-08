import Helper
import math

class Problem41:
    def run(self):
        n = 9
        max = 0
        while True:
            n = n - 1
            for perm in Helper.listPermutations(n):
                if Helper.isPrime(int(perm)):
                    if int(perm) > max:
                        max = int(perm)
            if max > 0:
                print(max)
                break
            

if __name__ == '__main__':
    solver = Problem41()
    solver.run()