import unittest
import Problem38

class Test(unittest.TestCase):
    def testIsReducable(self):
        solver = Problem38.Problem38()

        positives = [192384576, 918273645, 123456789]
        for pos in positives:
            self.assertTrue(solver.isReducable(pos))
        
        negatives = [765123489, 987654321]
        for neg in negatives:
            self.assertFalse(solver.isReducable(neg))
            
    def testIsPandigital(self):
        solver = Problem38.Problem38()
        
        positives = [192384576, 918273645, 123456789]
        for pos in positives:
            self.assertTrue(solver.isPandigital(pos))
        
        negatives = [1, 3423512387, 123456788, 999999999]
        for neg in negatives:
            self.assertFalse(solver.isPandigital(neg))
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()