import numpy as np 

def function(x):

	h5 = 7
	s7 = x
	paths = []
	try:
		if h5 > 2:
			s7 = s7+4
			x = 7*x
			paths.append(1)
		else:
			h5 = h5*s7
			x = 5*4
			h5 = 0*h5
			paths.append(2)
		if s7 < 9:
			h5 = x+h5
			h5 = 6-s7
			paths.append(3)
		else:
			x = 5+5
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