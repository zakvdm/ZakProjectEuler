class Problem:
    def isPalindrome(self, n):
        n = str(n)
        l = int(len(n) / 2)
        for i in range(0, l):
            if n[i] != n[(-1 * i) - 1]:
                return False
        return True
    
    def reverse(self, n):
        n = str(n)
        reversed = ""
        l = len(n)
        for i in range(0, l):
            reversed = reversed + n[l - 1 - i]
        return reversed
                
    def isLychrelNumber(self, n):
        for i in range(0, 50):
            n = n + int(self.reverse(n))
            if self.isPalindrome(n):
                return False
        return True
        
    def run(self):
        count = 0
        for i in range(0, 10000):
            if i > 0 and i % 1000 == 0:
                print(str((i / 10000) * 100) + '%')
            if self.isLychrelNumber(i):
                count = count + 1
        print(count)

if __name__ == '__main__':
    solver = Problem()
    solver.run()