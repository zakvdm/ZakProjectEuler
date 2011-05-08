PROBLEM_NUMBER = 50

ProblemName = 'Problem' + str(PROBLEM_NUMBER)
module = __import__(ProblemName)
solver = getattr(module, ProblemName)()
solver.run()