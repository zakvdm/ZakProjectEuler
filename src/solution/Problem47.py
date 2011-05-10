import Helper
import math

class Problem47:
    def run(self):
        CONS = 4
        primes = [2, 3, 5, 7, 11, 13, 17, 19]
        n = 19
        consecutive = 0
        # Counting up
        while True:
            n = n + 1
            
            if Helper.isPrime(n):
                primes.append(n)
                consecutive = 0
                continue
            
            # loop through primes
            count = 0
            #ps = []
            for p in primes:
                if n % p == 0:
                    count = count + 1
                    #ps.append(p)
                if count == CONS:
                    #print('at n=' + str(n) + ' with consecutive: ' + str(consecutive))
                    consecutive = consecutive + 1
                    #print(ps)
                    break
            
            if count != CONS: # We didn't find distinct prime factors...
                consecutive = 0
            
            if consecutive == CONS:
                print(n)
                return
                                

if __name__ == '__main__':
    solver = Problem47()
    solver.run()