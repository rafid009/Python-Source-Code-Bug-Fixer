import numpy as np 

def function(x):

	s0 = 4
	h5 = 2
	paths = []
	try:
		if s0 > 6:
			h5 = s0+3
			s0 = s0+5
			h5 = h5+0
			paths.append(1)
		else:
			s0 = s0-x
			s0 = s0-1
			x = 1+s0
			paths.append(2)
		if s0 >= 7:
			h5 = h5*s0
			paths.append(3)
		else:
			s0 = 9+s0
			s0 = 5+s0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h5 = x**0.5
		return h5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))