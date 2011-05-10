import Helper
import math

class Problem30:
    def run(self):
        candidate = 1
        matches = []
        while True:
            candidate = candidate + 1
            chars = Helper.numberToDigits(candidate)
            sum = 0
            for char in chars:
                sum = math.pow(int(char), 5) + sum
                
            if sum == candidate:
                print(sum)
                matches.append(sum)
                total = 0
                for match in matches:
                    total = total + match
                print('current sum: ' + str(total))
                
            if candidate % 100000 == 0:
                print('At candidate ' + str(candidate))
                
            
                
        
    
if __name__ == '__main__':
    solver = Problem30()
    solver.run()