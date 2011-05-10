class Problem():
    def triangle(self, n):
        # Triangle        P3,n=n(n+1)/2       1, 3, 6, 10, 15, ...
        return int((n * (n + 1)) / 2)

    def square(self, n):
        # Square          P4,n=n^2         1, 4, 9, 16, 25, ...
        return n**2

    def pentagonal(self, n):
        # Pentagonal      P5,n=n(3n−1)/2      1, 5, 12, 22, 35, ...
        return int((n * ((3 * n) - 1)) / 2)

    def hexagonal(self, n):
        # Hexagonal       P6,n=n(2n−1)        1, 6, 15, 28, 45, ...
        return (n * ((2 * n) - 1))

    def heptagonal(self, n):
        # Heptagonal      P7,n=n(5n−3)/2      1, 7, 18, 34, 55, ...
        return int((n * ((5 * n) - 3)) / 2)

    def octagonal(self, n):
        # Octagonal       P8,n=n(3n−2)        1, 8, 21, 40, 65, ...
        return (n * ((3 * n) - 2))

    def findCycles(self, in_candidates, sets):
        if len(sets) > 0:
            current_set = sets[0]
        else:
            # Time to loop back - turn the first column into a list of candidates
            current_set = [candidate[0] for candidate in in_candidates]

        out_candidates = []
        for candidate in in_candidates:
            left = candidate[-1]
            for right in current_set:
                if str(left)[2:] == str(right)[:2]:
                    out_candidates.append(candidate + [right])

        if len(sets) > 0:
            return self.findCycles(out_candidates, sets[1:])

        return out_candidates

    def generate_combinations(self):
        combinations = [[1], [2], [3], [4], [5]]

        while len(combinations[0]) < 5:
            new_combinations = []
            for comb in combinations:
                for no in range(1, 6):
                    if no in comb:
                        continue
                    new_combinations.append(comb + [no])
            combinations = new_combinations
        print(len(combinations))
        return combinations
              

    def run(self):
        triangles = []
        squares = []
        pentagonals = []
        hexagonals = []
        heptagonals = []
        octagonals = []

        n = 5
        while True:
            n = n + 1
            triangle = self.triangle(n)
            square = self.square(n)
            pentagonal = self.pentagonal(n)
            hexagonal = self.hexagonal(n)
            heptagonal = self.heptagonal(n)
            octagonal = self.octagonal(n)

            if len(str(triangle)) > 4 and len(str(square)) > 4 and len(str(pentagonal)) > 4 and len(str(hexagonal)) > 4 and len(str(heptagonal)) > 4 and len(str(octagonal)) > 4:
                break

            if len(str(triangle)) == 4:
                triangles = triangles + [triangle]
            if len(str(square)) == 4:
                squares = squares + [square]
            if len(str(pentagonal)) == 4:
                pentagonals = pentagonals + [pentagonal]
            if len(str(hexagonal)) == 4:
                hexagonals = hexagonals + [hexagonal]
            if len(str(heptagonal)) == 4:
                heptagonals = heptagonals + [heptagonal]
            if len(str(octagonal)) == 4:
                octagonals = octagonals + [octagonal]

        print("Finished populating initial lists...")

        initial_candidates = [[no] for no in triangles]
        combinations = self.generate_combinations()
        sets = [squares, pentagonals, hexagonals, heptagonals, octagonals]

        all_candidates = []
        for combination in combinations:
            s = [sets[i - 1] for i in combination]
            candidates = self.findCycles(initial_candidates, s)
            solutions = [candidate for candidate in candidates if candidate[0] == candidate[-1]]
            if len(solutions) > 0:
                print(solutions[0][:-1])
                return

        print("FAILED!")



if __name__ == '__main__':
    problem = Problem()
    problem.run()
