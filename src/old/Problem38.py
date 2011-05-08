import Helper
import math

class Problem38:
    def isReducable(self, number):
        # Tries to write number in form:
        #   x * (1, 2, ... ,n) where n > 1
        # Assumes a valid pandigital number is passed in
        number = str(number)
        
        for i in range(1, 6):
            candidate = int(number[0:i])
            testNumber = ''
            j = 1
            while len(testNumber) < 9:
                testNumber = testNumber + str(candidate * j)
                j = j + 1
            
            if testNumber == number:
                return True
            
        return False
    
    def isPandigital(self, number):
        number = str(number)
        for i in range(1, 10):
            if number.count(str(i)) != 1:
                return False
            
        return True
    
    def listPermutations(self, n):
        if n == 2:
            return ['12', '21']
        
        permutations = []
        for perm in self.listPermutations(n - 1):
            for i in range(0, len(perm) + 1):
                leftside = perm[:i]
                rightside = perm[len(leftside):]
                permutations.append(leftside + str(n) + rightside)
                
        return permutations
        
    def run(self):
        perms = self.listPermutations(8)
        
        max = 0
        for perm in perms:
            if self.isReducable('9' + perm):
                if int(perm) > max:
                    max = int(perm)
                    
        print('9' + str(max))


if __name__ == '__main__':
    solver = Problem38()
    solver.run()