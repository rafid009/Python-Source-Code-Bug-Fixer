import numpy as np 

def function(x):

	g3 = 7
	s0 = 8
	paths = []
	try:
		if s0 <= 9:
			g3 = g3*s0
			x = x/6
			paths.append(1)
		else:
			x = g3+x
			x = 9*x
			paths.append(2)
		if x <= 9:
			s0 = 1*x
			paths.append(3)
		else:
			x = x-7
			g3 = g3/2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s0 = x**0.5
		return s0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))