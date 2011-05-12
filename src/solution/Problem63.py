import math

class Problem:
    def run(self):
        # 10^1 = 10, 10^2 = 100, therefore 10 is our upperbound
        count = 0
        for i in range(1, 10):
            exp = 1
            while len(str(i**exp)) == exp:
                exp = exp + 1
                print(i)
                count = count + 1
        
        print(count)


if __name__ == '__main__':
    solver = Problem()
    solver.run()