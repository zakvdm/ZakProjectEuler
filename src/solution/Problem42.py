import Helper
import math

class Problem42:
    letterScores = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}
    triangleNumbers = [1]
    
    def cacheTriangleNumbers(self):
        for i in range(2, 1000):
            self.triangleNumbers.append(self.triangleNumbers[-1] + i)
            
        print(self.triangleNumbers)
        
    def getWords(self, filePath):
        wordsFile = open(filePath, 'r')
        words = wordsFile.read().split(',')
        words = [word.strip('\"') for word in words]
        #words.sort()
        return words

    def isTriangleWord(self, word):
        score = 0
        for ch in word:
            score = score + self.letterScores[ch]
            
        return self.triangleNumbers.count(score) > 0
        
        

    def run(self):
        self.cacheTriangleNumbers()
        words = self.getWords('../42words.txt')
        
        print(len(words))
        
        count = 0
        for word in words:
            if self.isTriangleWord(word):
                count = count + 1
        print(count)
            

if __name__ == '__main__':
    solver = Problem42()
    solver.run()