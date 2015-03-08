import OrderedSet

# Bittorrent job interview question:
# 40 bowls, equidistant
# place 9 oranges in bowls so that no 3 oranges, A, B, and C, are spaced such that dist(A, B) == dist(B, C)
class Problem:
    maxBowlNumber = 41
    maxOrangeNumber = 9
    solutions = 0

    def isAcceptable(self, oranges):
        i = 0
        while i < len(oranges) - 2:
            A = oranges[i]
            for indexB in range(i + 1, len(oranges) - 1):
                B = oranges[indexB]
                dist = B - A
                prohibitedC = B + dist
                if prohibitedC in oranges:
                    return False
            i = i + 1
        return True

    def placeOrange(self, bowlNumber, oranges):
        if not self.isAcceptable(oranges):
            #print("Solution not acceptable:")
            #print(oranges)
            return

        if len(oranges) == self.maxOrangeNumber:
            #print("Found a solution")
            #print(oranges)
            self.solutions = self.solutions + 1
            if self.solutions % 100 == 0:
                print("Found solutions: " + str(self.solutions))
                print(oranges)
            return

        if bowlNumber == self.maxBowlNumber:
            #print("Ran out of bowls:")
            #print(oranges)
            return

        # Don't place an orange in this bowl:
        copy = list(oranges)
        self.placeOrange(bowlNumber + 1, copy)

        # Place an orange in this bowl:
        oranges.append(bowlNumber)
        self.placeOrange(bowlNumber + 1, oranges)
                    
    def run(self):
        self.placeOrange(1, [])
                


if __name__ == '__main__':
    solver = Problem()
    solver.run()
