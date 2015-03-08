import Helper
import math

class Problem50:
    def run(self):
        MAX = 1000000
        
        primesDict = Helper.primesLessThan(MAX);
        primes = [p for p in primesDict.keys() if primesDict[p]]
        maxSequence = 2
        print(len(primes))
        for i in range(0, len(primes)):
            if len(primes) - i < maxSequence:
                break
            sum = primes[i]
            j = i
            while True:
                j = j + 1
                sum = sum + primes[j]
                if sum >= MAX:
                    break
                seqLength = j - i + 1
                if primesDict[sum] and seqLength > maxSequence:
                    print("Found new max sequence: p=" + str(sum) + " seqLength=" + str(seqLength) + " seqStart=" + str(primes[i]))
                    maxSequence = seqLength
            
if __name__ == '__main__':
    solver = Problem50()
    solver.run()