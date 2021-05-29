import numpy as np 

def function(x):

	h7 = 5
	s0 = x
	paths = []
	try:
		if h7 >= 8:
			x = 5/x
			x = h7*x
			paths.append(1)
		else:
			x = x-h7
			paths.append(2)
		if h7 > 2:
			x = 0*7
			h7 = s0*5
			x = x-7
			paths.append(3)
		else:
			s0 = s0-4
			s0 = 7+6
			paths.append(4)
		paths.append(5)
		assert s0 >= 0
		h7 = s0**0.5
		return h7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))