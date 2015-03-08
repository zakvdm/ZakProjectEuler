class Problem:
    results = {1:1, 89:89}
    def calcChain(self, i):
        if self.results.get(i) is None:
            nextInChain = 0
            for k in range(0, len(str(i))):
                nextInChain = nextInChain + int(str(i)[k])**2
            self.results[i] = self.calcChain(nextInChain)
            return self.results[i]
        else:
            return self.results[i]
            
    def run(self):
        # Taking sum of squares of each digit in 9,999999 = 567, so 567 is our "first order" upperbound
        print('caching results...')
        for i in range(1, 568):
            self.calcChain(i)

        print('counting...')
        count = 0
        for i in range(1, 10000000):
            if i % 500000 == 0:
                print(str((i / 10000000) * 100) + '%')
            num = 0
            for k in range(0, len(str(i))):
                num = num + int(str(i)[k])**2
            if self.results[num] == 89:
                count = count + 1
        
        print(count)
        


if __name__ == '__main__':
    solver = Problem()
    solver.run()