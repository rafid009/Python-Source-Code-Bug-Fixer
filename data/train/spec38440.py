import numpy as np 

def function(x):

	e2 = 4
	s0 = x
	paths = []
	try:
		if x <= 0:
			s0 = s0-5
			paths.append(1)
		else:
			e2 = e2-3
			x = x*s0
			paths.append(2)
		if x < 1:
			x = e2*x
			e2 = 8-e2
			paths.append(3)
		else:
			x = 3-2
			s0 = 3+9
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