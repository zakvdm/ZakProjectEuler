import math
from collections import defaultdict

class Problem:

    solutions = set()

    def findNumbersThatAddTo(self, numbersUpTo, targetSum):
        triplets = set()

        for left in range(1, numbersUpTo + 1):
            for middle in range(left + 1, numbersUpTo + 1):
                for right in range(middle + 1, numbersUpTo + 1):
                    if left + middle + right == targetSum:
                        triplets.add((left, middle, right))
                        triplets.add((left, right, middle))
                        triplets.add((middle, left, right))
                        triplets.add((middle, right, left))
                        triplets.add((right, middle, left))
                        triplets.add((right, left, middle))

        return triplets

    def findSolution(self, triplets, currentSolution, solutionLength):
        if len(currentSolution) == solutionLength:
            if currentSolution[-1][2] == currentSolution[0][1]:
                self.solutions.add(self.normalizeSolution(currentSolution))
            return

        for triplet in triplets:
            lastTriplet = currentSolution[-1]

            if lastTriplet[2] == triplet[1]:
                cloneTriplets = triplets.copy()
                cloneCurrentSolution = list(currentSolution)
                cloneCurrentSolution.append(triplet)
                cloneTriplets = self.removeSimilar(cloneTriplets, triplet)
                self.findSolution(cloneTriplets, cloneCurrentSolution, solutionLength)

    def removeSimilar(self, triplets, targetTriplet):
        to_remove = list()
        for triplet in triplets:
            left = triplet[0]
            if left == targetTriplet[0] or left == targetTriplet[1] or left == targetTriplet[2]:
                to_remove.append(triplet)
        for triplet in to_remove:
            triplets.remove(triplet)
        return triplets

    def normalizeSolution(self, solution):
        #print("normalizing: " + str(solution))
        min_i = 0
        minTriplet = solution[0]
        for i in range(1, len(solution)):
            if solution[i] < minTriplet:
                minTriplet = solution[i]
                min_i = i

        normalized_solution = []
        for k in range(0, len(solution)):
            index = (min_i + k) % len(solution)
            normalized_solution.append(solution[index])

        #print("normalized to: " + str(normalized_solution))
        return tuple(normalized_solution)

    def run(self):
        numberUpTo = 10
        targetSum = 12
        numberOfTriplets = 5
        #numberUpTo = 6
        #targetSum = 8
        #numberOfTriplets = 3

        maxSum = (3 * numberUpTo)

        while targetSum < maxSum:
            targetSum = targetSum + 1
            triplets = self.findNumbersThatAddTo(numberUpTo, targetSum)
            if len(triplets) < numberOfTriplets:
                print("Not enough triplets")


            for firstTriplet in triplets:
                cloneTriplets = triplets.copy()
                cloneTriplets = self.removeSimilar(cloneTriplets, firstTriplet) # Make sure similar triplets aren't available for this recursion
                self.findSolution(cloneTriplets, [firstTriplet], numberOfTriplets)

        #for solution in self.solutions:
            #print(solution)

        #max_solution = ((1, 6, 10), (3, 10, 4), (7, 4, 6)) # random _LOW_ solution
        max_solution = (0, 0, 0)
        for solution in self.solutions:
            if solution > max_solution:
                max_solution = solution

        print("##### MAX SOLUTION: ")
        print(max_solution)
        ans = ""
        for tup in list(max_solution):
            for val in list(tup):
                ans = ans + str(val)
        print(ans)
        print("#####")

        for solution in self.solutions:
            if solution[0] > (6, 0, 0):
                print(solution)
        return



if __name__ == '__main__':
    solver = Problem()
    solver.run()
