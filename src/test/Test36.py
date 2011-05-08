import unittest
import Problem36

class Test(unittest.TestCase):
    def testConvertToBinary(self):
        solver = Problem36.Problem36()
        
        self.assertEqual('1001001001', solver.convertToBinary(585))
        self.assertEqual('0', solver.convertToBinary(0))
        self.assertEqual('1', solver.convertToBinary(1))
        self.assertEqual('10', solver.convertToBinary(2))
        self.assertEqual('11', solver.convertToBinary(3))
        
    def testIsPalindrome(self):
        solver = Problem36.Problem36()
        
        self.assertTrue(solver.isPalindrome('1001001001'))
        self.assertTrue(solver.isPalindrome(585))
        self.assertTrue(solver.isPalindrome(3))
        
        self.assertFalse(solver.isPalindrome('0110'))



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()