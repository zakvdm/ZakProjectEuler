import math

class Problem53:
    
    def nCr(self, n, r):
        return math.factorial(n) / (math.factorial(r) * math.factorial(n - r))
                    
        
    def run(self):
        count = 0
        for n in range(23, 101):
            for r in range(2, n):
                if self.nCr(n, r) > 1000000:
                    count = count + 1
                    
        print(count)


if __name__ == '__main__':
    solver = Problem53()
    solver.run()