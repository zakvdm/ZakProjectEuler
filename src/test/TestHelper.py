'''
Created on 18 Mar 2010

@author: zak
'''
import unittest
import Helper

class Test(unittest.TestCase):
    def testPrimeCheck(self):
        # Ignores negatives:
        self.assertFalse(Helper.isPrime(-1))
        self.assertFalse(Helper.isPrime(-7))
        
        # Normal primes:
        primes = [1, 2, 3, 5, 7, 1601]
        for prime in primes:
            self.assertTrue(Helper.isPrime(prime))
            
        nonPrimes = primes = [4, 6, 8, 9, 10, 100]
        for nonprime in nonPrimes:
            self.assertFalse(Helper.isPrime(nonprime))
            
    def testNumberToDigits(self):
        self.assertEqual(['3','4','9','4','0','1'], Helper.numberToDigits(349401))
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testPrimeCheck']
    unittest.main()