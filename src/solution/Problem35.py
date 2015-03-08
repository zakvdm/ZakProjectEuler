import Helper

class Problem35:
    def cycle(self, number):
        if len(str(number)) == 1:
            return number
        
        return str(number)[1:] + str(number)[0]
    
    def run(self):
        print('Caching primes...')
        # NOTE: This is slow right now... To speed this up, I guess I should check if it's cyclical
        #        while calculating the primes
        primes = Helper.primesLessThan(1000000)
        print('Finding cyclical primes...')
        count = 0
        iterations = 0
        for prime in primes:
            if prime == 1:
                continue

            iterations = iterations + 1
            if iterations % 10000 == 0:
                print("I'm up to: " + str(prime))
                        
            if primes[prime]:
                next_prime = self.cycle(prime)
                is_circular = True
                counter = 0
                while int(next_prime) != prime:
                    counter = counter + 1
                    if counter > 1000:
                        print('I seem to be stuck:')
                        print(prime)
                        print(next_prime)
                    if not primes[int(next_prime)]:
                        is_circular = False
                    next_prime = self.cycle(next_prime)    
                    
                if is_circular:
                    count = count + 1
                    
        print(count)
    
if __name__ == '__main__':
    solver = Problem35()
    solver.run()
