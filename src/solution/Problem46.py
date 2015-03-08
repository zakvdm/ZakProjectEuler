import Helper
import math

class Problem46:
    def run(self):
        primes = [2, 3, 5, 7, 11, 13, 17, 19]
        twosquares = [2, 8, 18]
        nextsquare = 4
        # Loop over all numbers N
        n = 8
        while True:
            n = n + 1
            if n % 1000 == 0:
                print(n)
            # If prime, add to list of primes
            if Helper.isPrime(n):
                primes.append(n)
                continue
            # Check that we've cached enough 2x squares
            while twosquares[-1] < n:
                twosquares.append(2 * (nextsquare * nextsquare))
                nextsquare = nextsquare + 1
            
            found = False
            
            if n % 2 == 0:
                found = True
            # Loop over all primes P less than N
            for p in primes:
                if found:
                    break
                # Loop over all cached 2x squares K less than N
                for doublesquare in twosquares:
                    if found:
                        break
                    # If P + K = N: continue
                    if p + doublesquare == n:
                        found = True
                        
                    if p + doublesquare > n:
                        break
            
            # If we get to the end, print N and exit
            if not found:            
                print('OOPS!')
                print(str(n) + " couldn't be written as the sum of a prime and double a square")
                return

        
                    

if __name__ == '__main__':
    solver = Problem46()
    solver.run()