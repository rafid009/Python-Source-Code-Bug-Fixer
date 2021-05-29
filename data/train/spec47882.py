import numpy as np 

def function(x):

	e0 = 6
	s0 = x
	paths = []
	try:
		if e0 < 4:
			e0 = e0*x
			paths.append(1)
		else:
			s0 = s0-8
			e0 = e0-6
			paths.append(2)
		if x >= 6:
			s0 = s0*9
			s0 = s0-s0
			x = x*5
			paths.append(3)
		else:
			e0 = 7*3
			s0 = s0/9
			e0 = e0+e0
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