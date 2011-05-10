import Helper
import math

class Problem48:
    def run(self):
        #print(1000**1000)
        try:
            MAX = 1000
            sum = 0
            for i in range(1, MAX + 1):
                sum = (sum + i**i) % 100000000000
        except:
            print('OOPS')
            print(i)
            
        print(sum)

if __name__ == '__main__':
    solver = Problem48()
    solver.run()