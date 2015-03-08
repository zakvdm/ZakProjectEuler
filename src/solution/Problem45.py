import math

class Problem45:
    pents = {}
    pentList = []
    biggestPent = 0
    def cachePentagonals(self, n):
        for i in range(1, n):
            self.biggestPent = self.findPentagonal(i)
            self.pents[self.biggestPent] = True
            
    def findTriangle(self, n):
        return int(n * (n + 1) / 2)
    def findPentagonal(self, n):
        return int(n * (3*n - 1) / 2)
    def findHexagonal(self, n):
        return int(n * (2*n - 1))
    
    def solveQuadraticPentagonal(self, n):
        a = 3
        b = -1
        c = -1 * (2*n)
        return self.solveQuadratic(a, b, c)
    def solveQuadraticHexagonal(self, n):
        a = 2
        b = -1
        c = -1 * n
        return self.solveQuadratic(a, b, c)
    def solveQuadratic(self, a, b, c):
        det = (b * b) - (4 * a * c)
        if det <= 0:
            return (False, 0, 0)
        sqrt = math.sqrt(det)
        return (True, (-1 * b + sqrt) / (2 * a), (-1 * b - sqrt) / (2 * a))
    
    def isValidAnswer(self, quadTuple):
        if quadTuple[0]:
            if int(quadTuple[1]) == quadTuple[1] and quadTuple[1] > 0:
                return True
            if int(quadTuple[2]) == quadTuple[2] and quadTuple[2] > 0:
                return True
        return False
        
    def run(self):
        print(self.findTriangle(285) == self.findPentagonal(165) == self.findHexagonal(143))
        print(self.solveQuadraticPentagonal(40755))
        print(self.solveQuadraticHexagonal(40755))
        print(self.isValidAnswer(self.solveQuadraticPentagonal(40755)) and self.isValidAnswer(self.solveQuadraticHexagonal(40755)))
        
        x = 285
        while True:
            x = x + 1
            triangleNumber = self.findTriangle(x)
            if self.isValidAnswer(self.solveQuadraticPentagonal(triangleNumber)) and self.isValidAnswer(self.solveQuadraticHexagonal(triangleNumber)):
                print(x)
                print(triangleNumber)
                print(self.solveQuadraticPentagonal(triangleNumber))
                print(self.solveQuadraticHexagonal(triangleNumber))
                return
            

if __name__ == '__main__':
    solver = Problem45()
    solver.run()