class Problem31:
    coins = (200, 100, 50, 20, 10, 5, 2, 1)
    
    def run(self):
        print(self.solve(200, 200, ""))
        #print(self.partialValues[10])
        #print(self.partialValues[5])
        #print(self.partialValues[3])
        #print(self.partialValues[2])
        
    def solve(self, value, maxvalue, text):
        valueCombinations = 0
        for coin in self.coins:
            if coin > maxvalue:
                continue
            
            if value - coin == 0:
                valueCombinations = valueCombinations + 1
                #print(text + '.' + str(coin))
                
            if value - coin > 0:
                valueCombinations = valueCombinations + self.solve(value - coin, coin, text + '.' + str(coin))
        
        return valueCombinations
        
    
    
if __name__ == '__main__':
    solver = Problem31()
    solver.run()