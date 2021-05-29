import numpy as np 

def function(x):

	s0 = x
	n8 = x
	paths = []
	try:
		if s0 > 8:
			s0 = s0+1
			s0 = 5*s0
			paths.append(1)
		else:
			s0 = 1/s0
			s0 = s0*3
			paths.append(2)
		if s0 > 1:
			s0 = 2+s0
			paths.append(3)
		else:
			n8 = s0-s0
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