import unittest
import Problem35

class Test(unittest.TestCase):


    def testCycle(self):
        solver = Problem35.Problem35()
        
        self.assertEqual('971', solver.cycle(197))
        self.assertEqual('719', solver.cycle(971))
        self.assertEqual('197', solver.cycle(719))
        
        self.assertEqual('011', solver.cycle(101))


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()