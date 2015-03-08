import unittest
import Problem33

class Test(unittest.TestCase):
    def testCommonNumber(self):
        solver = Problem33.Problem33()
        
        self.assertEqual(9, solver.fractionHasCommonNumberInNumeratorAndDenominator(49, 98))
        self.assertEqual(4, solver.fractionHasCommonNumberInNumeratorAndDenominator(43, 41))
        
        self.assertEqual(0, solver.fractionHasCommonNumberInNumeratorAndDenominator(30, 50))

    def testIsCuriousFraction(self):
        solver = Problem33.Problem33()
        
        self.assertTrue(solver.isCuriousFraction(49, 98, 9))
        
        self.assertFalse(solver.isCuriousFraction(83, 31, 3))
        self.assertFalse(solver.isCuriousFraction(11, 11, 1))

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()