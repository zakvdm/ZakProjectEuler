import unittest
import Problem32

class Test(unittest.TestCase):
    def testIsPanDigital(self):
        solver = Problem32.Problem32()
        
        # YES:
        self.assertTrue(solver.isPanDigital(123456789))
        self.assertTrue(solver.isPanDigital(321654987))
        self.assertTrue(solver.isPanDigital('123987564'))
        
        # OVER 9 DOESN'T WORK:
        self.assertFalse(solver.isPanDigital(1234598761))
        
        # NO:
        self.assertFalse(solver.isPanDigital(23))
        self.assertFalse(solver.isPanDigital(1231456789))
        self.assertFalse(solver.isPanDigital(231455789))
        self.assertFalse(solver.isPanDigital(12345678))
        
    def testAllDigitsUnique(self):
        solver = Problem32.Problem32()
        
        self.assertTrue(solver.allDigitsUnique(325))
        self.assertTrue(solver.allDigitsUnique(1))
        self.assertTrue(solver.allDigitsUnique(823451))
        
        self.assertFalse(solver.allDigitsUnique(22))
        self.assertFalse(solver.allDigitsUnique(34525))


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()