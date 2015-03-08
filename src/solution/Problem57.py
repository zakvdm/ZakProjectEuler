class Problem:
    def recursiveRootTwo(self, n, maxNoOfIterations):
        if n == 0:
            fraction = self.recursiveRootTwo(n + 1, maxNoOfIterations)
            flippedFraction = (fraction[1], fraction[0])
            return (flippedFraction[1] + flippedFraction[0], flippedFraction[1])
        if n == maxNoOfIterations:
            return (2, 1)
        fraction = self.recursiveRootTwo(n + 1, maxNoOfIterations)
        flippedFraction = (fraction[1], fraction[0])
        
        return ((2 * flippedFraction[1]) + flippedFraction[0], flippedFraction[1]) 
                        
    def run(self):
        fraction = self.recursiveRootTwo(0, 8)
        print(len(str(fraction[0])) > len(str(fraction[1])))
        count = 0
        for i in range(1, 1001):
            print(i)
            fraction = self.recursiveRootTwo(0, i)
            if len(str(fraction[0])) > len(str(fraction[1])):
                count = count + 1
        print(count)
        

if __name__ == '__main__':
    solver = Problem()
    solver.run()