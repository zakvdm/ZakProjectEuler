import math
from collections import defaultdict

class Problem:
    def recurse(self, a0, a, prev_p, p, prev_q, q, P, Q, D):
        next_P = (a * Q) - P
        next_Q = (D - (next_P**2)) / Q
        next_a = math.floor((a0 + next_P) / next_Q)

        next_p = (next_a * p) + prev_p
        next_q = (next_a * q) + prev_q

        return next_a, p, next_p, q, next_q, next_P, next_Q

    def run(self):
        n = 1
        maxX = 0

        while n <= 1000:
            n = n + 1
            if math.sqrt(n) == int(math.sqrt(n)):
                continue
            if n % 100 == 0:
                print(".")
           
            print("Solving for D = {d}".format(d=n))

            D = n
            a0 = math.floor(math.sqrt(D))
            p0 = a0
            q0 = 1
            P0 = 0
            P1 = a0
            Q0 = 1
            Q1 = D - (a0**2)
            a1 = math.floor((a0 + P1) / Q1)
            p1 = (a0 * a1) + 1
            q1 = a1

            a = a1
            prev_p = p0
            p = p1
            prev_q = q0
            q = q1
            P = P1
            Q = Q1

            r = 0
            target_r = -1
            while True:
                #print("a = {a}, p = {p}, q={q}, P={P}, Q={Q}".format(a=a, p=p, q=q, P=P, Q=Q))
                a, prev_p, p, prev_q, q, P, Q = self.recurse(a0, a, prev_p, p, prev_q, q, P, Q, D)

                r = r + 1
                if target_r == -1 and a == 2 * a0:
                    #print("Now periodic: a = {a} & r = {r}".format(a=a, r=r))
                    if r % 2 == 1:
                        if prev_p > maxX:
                            print("Solution with r odd: {p} & {q}".format(p=prev_p, q=prev_q))
                            maxX = prev_p
                            print("Found new biggest X for D = {D}".format(D=n))
                        
                        break
                    else:
                        target_r = int(2 * r) + 1
                        #print("###### Even land - %d & r = %d" % (target_r, r))


            
                if int(r) == target_r:
                    if prev_p > maxX:
                        print("Even solution: {p} & {q}".format(p=prev_p, q=prev_q))
                        maxX = prev_p
                        print("Found new biggest X for D = {D}".format(D=n))
                    break


if __name__ == '__main__':
    solver = Problem()
    solver.run()
