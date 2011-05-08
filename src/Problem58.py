import Helper

class Problem:
    primes = 0
    totalDiags = 1
    
    def calcRatio(self, diagonals):
        for candidate in diagonals:
            if Helper.isPrime(candidate):
                self.primes = self.primes + 1
        self.totalDiags = self.totalDiags + 4
    
    def getDiagonals(self, start, length):
        diagonals = [start + (length - 1)]
        for i in range(1, 4):
            diagonals.append(diagonals[-1] + (length - 1))
        return diagonals
    
    def run(self):
        print(self.getDiagonals(1, 3))
        print(self.getDiagonals(9, 5))
        print(self.getDiagonals(25, 7))
        diags = [1]
        for i in range(1, 100000):
            length = 1 + i * 2
            diags = self.getDiagonals(diags[-1], length)
            self.calcRatio(diags)
            print('length: ' + str(length) + ': ' + str(self.primes / self.totalDiags))
            
            
        
        

if __name__ == '__main__':
    solver = Problem()
    solver.run()