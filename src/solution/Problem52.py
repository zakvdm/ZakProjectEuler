class Problem52:
    
    def hasSameDigits(self, number1, number2):
        number1 = str(number1)
        number2 = str(number2)
        
        if len(number1) != len(number2):
            return False
        
        for i in range(0, len(number1)):
            if (number1.count(number1[i]) != number2.count(number1[i])):
                return False
            
        return True
                    
        
    def run(self):
        candidate = 1
        while True:
            candidate = candidate + 1
            if self.hasSameDigits(candidate, 2*candidate) and self.hasSameDigits(candidate, 3*candidate) and self.hasSameDigits(candidate, 4*candidate) and self.hasSameDigits(candidate, 5*candidate) and self.hasSameDigits(candidate, 6*candidate):
                print(candidate)
                return


if __name__ == '__main__':
    solver = Problem52()
    solver.run()