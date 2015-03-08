
class Problem32:
    def isPanDigital(self, number):
        numberString = str(number)
        for digit in range(1, 10):
            if numberString.count(str(digit)) != 1:
                return False
        return True
    
    def allDigitsUnique(self, number):
        numberString = str(number)
        for ch in numberString:
            if numberString.count(ch) != 1:
                return False
            
        return True
            
        
        
    def run(self):
        for lhs in range(1, 9999):
            if lhs % 100 == 0:
                print('Testing with lhs: ' + str(lhs))
            if self.allDigitsUnique(lhs):

                for rhs in range(lhs, 9999):
                    if self.allDigitsUnique(rhs):
                        prod = lhs * rhs
                        if len(str(lhs) + str(rhs) + str(prod)) == 9:
                            if self.isPanDigital(str(lhs) + str(rhs) + str(prod)):
                                print(prod)
        pass
    
if __name__ == '__main__':
    solver = Problem32()
    solver.run()