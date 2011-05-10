import Helper
import math

class Problem39:
    def countPermutations(self, p):
        count = 0
        for a in range(1, int(p/3) + 1):
            for b in range(a, int(p/2) + 1):
                c = p - a - b
                if c == math.sqrt(a*a + b*b):
                    count = count + 1
                    
        return count
        
        
    def run(self):
        max = 0
        maxp = 0
        for p in range(5, 1001):
            if p % 100 == 0:
                print(p)
            solutions = self.countPermutations(p)
            if solutions > max:
                max = solutions
                maxp = p
        
        print(max)
        print(maxp)

if __name__ == '__main__':
    solver = Problem39()
    solver.run()