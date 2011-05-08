import math

def fibonacci(x):
  """
  >>> fibonacci(3)
  2
  >>> fibonacci(4)
  3
  >>> fibonacci(5)
  5
  >>> fibonacci(6)
  8
  >>> fibonacci(7)
  13
  >>> fibonacci(12)
  144
  >>> fibonacci(20)
  6765
  """
  if x == 1 or x == 2:
    return 1
  return fibonacci(x - 1) + fibonacci(x - 2)
    
def findAnswer():
  answers = [1, 1, 2]
  count = 3
  while len(str(answers[-1])) < 1000:
    count = count + 1
    newFib = answers[1] + answers[2]
    answers[0] = answers[1]
    answers[1] = answers[2]
    answers[2] = newFib
  
  print(answers)
  print('---')
  print(count)
    
def _test():
    import doctest
    doctest.testmod()

if __name__ == "__main__":
    _test()
    findAnswer()
