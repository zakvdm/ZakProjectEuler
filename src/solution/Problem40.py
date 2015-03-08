import Helper
import math

class Problem40:
    def run(self):
        wants = {1:0, 10:0, 100:0, 1000:0, 10000:0, 100000:0, 1000000:0}
        count = 0
        length = 0
        nextWant = 1
        while nextWant != 10000000:
            count = count + 1
            length = length + len(str(count))
            if length >= nextWant:
                index = length - nextWant
                wants[nextWant] = int(str(count)[-1 * index - 1])
                nextWant = nextWant * 10

        print(wants)

if __name__ == '__main__':
    solver = Problem40()
    solver.run()