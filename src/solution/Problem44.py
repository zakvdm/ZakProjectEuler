import Helper

class Problem44:
    pents = {}
    pentList = []
    biggestPent = 0
    def cachePentagonals(self, n):
        for i in range(1, n):
            self.biggestPent = self.findPentagonal(i)
            self.pents[self.biggestPent] = True
            
    def findPentagonal(self, n):
        return int(n * (3*n - 1) / 2)
    
    def run(self):
        self.pentList.append(self.findPentagonal(1))
        self.pents[self.pentList[-1]] = True
        self.pentList.append(self.findPentagonal(2))
        self.pents[self.pentList[-1]] = True
        for n in range(3,1000000):
            if n % 100000 == 0:
                print('.', end='')

            newPent = self.findPentagonal(n)
            self.pents[newPent] = True
            self.pentList.append(newPent)
            for lhs in self.pentList:
                if self.pents.get(newPent - lhs, False):
                    if self.pents.get(newPent - lhs - lhs, False):
                        print('MWAH!' + str(lhs) + ' ' + str(newPent - lhs))
            

if __name__ == '__main__':
    solver = Problem44()
    solver.run()