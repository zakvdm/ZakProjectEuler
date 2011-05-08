import math

class Problem34(object):
    candidate = 3
    while True:
        sum = 0
        for ch in str(candidate):
            sum = sum + math.factorial(int(ch))
            
        if sum == candidate:
            print(candidate)
            
        candidate = candidate + 1
        
        if candidate % 100000 == 0:
            print('.')

if __name__ == '__main__':
    solver = Problem34()
    solver.run()        