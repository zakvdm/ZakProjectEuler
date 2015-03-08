import Helper
import math

class Problem37:
    primes = Helper.primesLessThan(5000)
     
    def isPrimeReducable(self, number):
        number = str(number)
        
        if len(number) == 1:
            return False
        
        for i in range(0, len(number)):
            if not self.primes[int(number[i:])]:
                return False
            
        for i in range(1, len(number)):
            if not self.primes[int(number[:-1 * i])]:
                return False
        
        return True
        
        
    def run(self):
        max = 1000000
        self.primes = Helper.primesLessThan(max)
        
        count = 0
        for i in range (11, max):
            if self.isPrimeReducable(i):
                print(i)
                count = count + 1
        print(count)

if __name__ == '__main__':
    solver = Problem37()
    solver.run()