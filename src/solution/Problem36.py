import math

class Problem36:
    def convertToBinary(self, number):
        if number == 0:
            return '0'
        binaryVersion = ''
        exp = int(math.log(number, 2)) + 1
        while exp >= 0:
            if number / math.pow(2, exp) >= 1:
                number = number - math.pow(2, exp)
                binaryVersion = binaryVersion + '1'
            else:
                if binaryVersion != '':
                    binaryVersion = binaryVersion + '0'
            exp = exp - 1
        return binaryVersion
 
    def isPalindrome(self, number):
        number = str(number)
        if number[0] == '0':
            return False
        
        for i in range(0, int(len(number) / 2)):
            if number[i] != number[(-1 * i) - 1]:
                return False
            
        return True
        
        
    def run(self):
        sum = 0
        for i in range (1, 1000000):
            if self.isPalindrome(i):
                binNum = self.convertToBinary(i)
                if self.isPalindrome(binNum):
                    print(i)
                    sum = sum + i
        print(sum)

if __name__ == '__main__':
    solver = Problem36()
    solver.run()