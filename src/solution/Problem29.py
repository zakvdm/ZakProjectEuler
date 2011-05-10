import math
import collections

class Problem29(object):
    
    def run(self):
        d = collections.defaultdict()
        for a in range(2, 101):
            for b in range(2, 101):
                d[math.pow(a, b)] = True
                if a == b:
                    print(a)
                    
        print(len(d.keys()))
        
if __name__ == '__main__':
    solver = Problem29()
    solver.run()
        