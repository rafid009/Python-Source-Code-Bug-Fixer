import numpy as np 

def function(x):

	h7 = x
	s0 = x
	paths = []
	try:
		if h7 < 5:
			h7 = h7+s0
			h7 = 7-s0
			paths.append(1)
		else:
			x = x-3
			paths.append(2)
		if h7 < 3:
			s0 = 0+2
			paths.append(3)
		else:
			h7 = 0*6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))