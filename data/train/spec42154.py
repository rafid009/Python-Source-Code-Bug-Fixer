import numpy as np 

def function(x):

	j4 = 6
	s9 = 0
	paths = []
	try:
		if j4 < 7:
			s9 = x-8
			j4 = 1+2
			paths.append(1)
		else:
			x = x*x
			paths.append(2)
		if x >= 7:
			s9 = s9*9
			j4 = 7-x
			paths.append(3)
		else:
			j4 = 3/j4
			x = 2*x
			s9 = s9*7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s9 = x**0.5
		return s9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))