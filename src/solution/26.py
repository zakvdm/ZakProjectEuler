import math
from decimal import *

#precision = 1000
#getcontext().prec = precision

threshold = 3
maxMatch = [50]

def RecurringPortionOfFraction(x, precision):
  """
  >>> RecurringPortionOfFraction(2, 10)
  0
  >>> RecurringPortionOfFraction(3, 10)
  3
  >>> RecurringPortionOfFraction(4, 10)
  0
  >>> RecurringPortionOfFraction(5, 10)
  0
  >>> RecurringPortionOfFraction(6, 10)
  6
  >>> RecurringPortionOfFraction(7, 20)
  142857
  >>> RecurringPortionOfFraction(96, 20)
  6
  >>> RecurringPortionOfFraction(131, 500)
  0
  """
  getcontext().prec = precision
  numOriginal = str(Decimal(1)/Decimal(x))
  num = numOriginal
  # Pop the crap off the front:
  while num[0] == '0' or num[0] == '.':
    num = num[1:]
  maxMatchLength = len(num)
  matchSequence = num[0]
  num = num[1:]
  for i in range(0, len(num)):
    for j in range(0, len(matchSequence)):
      if matchSequence[j:] == num[:len(matchSequence) - j]:
        # Check if this is a legitimate match:
        trueMatch = True
        for k in range(0, threshold):
          offset = k * len(matchSequence[j:])
          if matchSequence[j:] != num[offset:offset + len(matchSequence[j:])]:
            #print(matchSequence[j:] + ' is not a True Sequence of ' + str(1/x))
            #print(matchSequence[j:] + ' != ' + num[offset:offset + len(matchSequence[j:])])
            trueMatch = False
            break

        if trueMatch:
          if len(matchSequence[j:]) > maxMatch[0]:
            maxMatch[0] = len(matchSequence[j:])
            print('Try number: ' + str(x))
            #print(numOriginal)
            #print('Match Sequence: ' + matchSequence[j:])
          return int(matchSequence[j:])

    matchSequence = matchSequence + num[0]
    num = num[1:]

  if len(matchSequence) == maxMatchLength == precision:
    return -1 * x
  return 0
   
def findAnswer():
  print(RecurringPortionOfFraction(983, 10000))
def findAnswer2():
  candidates = []
  for i in range(1, 1000):
  #for i in candidates:
    #print('Trying: ' + str(i))
    ans = RecurringPortionOfFraction(i, 100)
    if ans < 0:
      candidates.append(-1 * ans)

  print(candidates)
  candidates2 = []
  for j in candidates:
    ans = RecurringPortionOfFraction(j, 10000)
    if ans < 0:
      candidates2.append(-1 * ans)

  print(candidates2)

def _test():
    import doctest
    doctest.testmod()

if __name__ == "__main__":
    _test()
    findAnswer()
