import unittest
import Problem37

class Test(unittest.TestCase):
    def testIsPrimeReducable(self):
        solver = Problem37.Problem37()

        positives = [3797]
        for pos in positives:
            self.assertTrue(solver.isPrimeReducable(pos))
        
        negatives = [2, 3, 5, 7, 18, 237]
        for neg in negatives:
            self.assertFalse(solver.isPrimeReducable(neg))
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()