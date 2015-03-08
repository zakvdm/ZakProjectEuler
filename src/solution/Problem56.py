import math

class Problem:
    def sumOfDigits(self, n):
        n = str(n)
        sum = 0
        for i in range(0, len(n)):
            sum = sum + int(n[i])
        return sum
                        
    def run(self):
        maxSum = 0
        for a in range(0, 100):
            print(a)
            for b in range(0, 100):
                n = a ** b
                maxSum = max(self.sumOfDigits(n), maxSum)
        
        print('done!')
        print(maxSum)
        

if __name__ == '__main__':
    solver = Problem()
    solver.run()