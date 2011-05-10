import Helper

class Problem27:
    def calcQuadratic(self, n, arguments):
        return n**2 + arguments[0]*n + arguments[1]
    
    def biggestNStillPrime(self, a, b):
        n = 0
        while True:
            quad = self.calcQuadratic(n, (a, b))
            if (Helper.isPrime(quad)):
                n = n + 1
            else:
                return n - 1
    
    def findAnswer(self):
        candidates = Helper.primesLessThan(10000)
        bCandidates = [k for k in candidates if candidates[k] == True and k <= 1000]
        bCandidates.reverse()
        aCandidates = range(-999, 1000)
        
        print('Searching with a values: ' + str(aCandidates[0]) + ' <-> ' + str(aCandidates[-1]))
        
        maxPair = (0, 0)
        maxN = 0
        
        for b in bCandidates:
            print('Testing b candidate: ' + str(b))
            for a in aCandidates:
                n = self.biggestNStillPrime(a, b)
                if n > maxN:
                    print('New biggest n: ' + str(n) + ' for pair: ' + str(a) + ',' + str(b))
                    maxN = n
                    maxPair = (a, b)

        print(self.calcQuadratic(maxN, maxPair))
        

if __name__ == "__main__":
    runner = Problem27()
    runner.findAnswer()
