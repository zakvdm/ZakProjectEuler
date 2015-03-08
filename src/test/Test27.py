'''
Created on 18 Mar 2010

@author: zak
'''
import unittest
import Problem27

class Test27(unittest.TestCase):
    def testCalcQuadratic(self):
        prob = Problem27.Problem27()
        self.assertEqual(41, prob.calcQuadratic(0, (1, 41)))
        self.assertEqual(43, prob.calcQuadratic(1, (1, 41)))
        self.assertEqual(1681, prob.calcQuadratic(40, (1, 41)))
        self.assertEqual(1601, prob.calcQuadratic(79, (-79, 1601)))
        self.assertEqual(1681, prob.calcQuadratic(80, (-79, 1601)))
        
    def testBiggestNStillPrime(self):
        prob = Problem27.Problem27()
        self.assertEqual(39, prob.biggestNStillPrime(1, 41))
        self.assertEqual(79, prob.biggestNStillPrime(-79, 1601))
        self.assertEqual(0, prob.biggestNStillPrime(-997, 41))

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()