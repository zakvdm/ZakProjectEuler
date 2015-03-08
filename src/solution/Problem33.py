
class Problem33:
    def fractionHasCommonNumberInNumeratorAndDenominator(self, top, bottom):
        if top % 10 == 0:
            return False # These are 'trivial' examples that we want to ignore
        
        for ch in str(top):
            if str(bottom).count(ch) == 1:
                if str(top).count(ch) == 1:
                    return int(ch)
            
        return 0
    
    def isCuriousFraction(self, top, bottom, common):
        if top == bottom:
            return False
        
        new_top = int(str(top).replace(str(common), ''))
        new_bottom = int(str(bottom).replace(str(common), ''))
        
        if new_bottom == 0:
            return False
        
        return (top / bottom) == (new_top / new_bottom)
    
    def run(self):
        curiousFractions = []
        for top in range(11, 100):
            for bottom in range(top, 100):
                common = self.fractionHasCommonNumberInNumeratorAndDenominator(top, bottom)
                if common != 0 and self.isCuriousFraction(top, bottom, common):
                    curiousFractions.append((top, bottom))
                    print(str(top) + '/' + str(bottom))
        
        product = (1, 1)            
        for fraction in curiousFractions:
            product = (product[0] * fraction[0], product[1] * fraction[1])
            
        print(product) 
            
                    
                    
                
        
    
if __name__ == '__main__':
    solver = Problem33()
    solver.run()