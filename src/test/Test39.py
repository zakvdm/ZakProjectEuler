import unittest
import Problem39

class Test(unittest.TestCase):
    def testPermutations(self):
        solver = Problem39.Problem39()
        
        self.assertEqual(3, solver.countPermutations(120))
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()