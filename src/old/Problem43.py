import Helper

class Problem43:
    primes = [2,3,5,7,11,13,17]
    def isFunky(self, number):
        number = str(number)
        for i in range(1,8):
            if int(number[i:i+3]) % self.primes[i - 1] != 0:
                return False
        return True
    
    def run(self):
        funkies = []
        
        perms = Helper.listPermutationsWithZero(9)
        print(len(perms))
        count = 0
        for num in perms:
            count = count + 1
            if count % 100000 == 0:
                print(count, end=',')
            if self.isFunky(num):
                funkies.append(num)

        print('')
        print(funkies)
        sum = 0
        for funky in funkies:
            sum = sum + int(funky)
        
        print(sum)
            

if __name__ == '__main__':
    solver = Problem43()
    solver.run()