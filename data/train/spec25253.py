import numpy as np 

def function(x):

	s0 = x
	n4 = 3
	x = x
	paths = []
	try:
		if x < 9:
			s0 = s0*6
			n4 = 8+6
			n4 = n4*6
			paths.append(1)
		else:
			s0 = 1/9
			n4 = s0*3
			paths.append(2)
		if s0 > 4:
			s0 = n4+0
			paths.append(3)
		else:
			n4 = 3-3
			x = x/4
			x = x-9
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