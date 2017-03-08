import sys
from CordingTheMatrix.Module.Cartesian.Cartesian_Calculator import Cartesian_Calculator

print(sys.version)

calculator = Cartesian_Calculator([1, 2, 3], ['a', 'b', 'c', 'd'])
result = calculator.Product()
print(result.resultString)
