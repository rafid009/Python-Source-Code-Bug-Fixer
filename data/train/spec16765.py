import numpy as np 

def function(x):

	y0 = x
	h0 = 0
	paths = []
	try:
		if h0 >= 6:
			h0 = h0*6
			paths.append(1)
		else:
			h0 = 9*y0
			h0 = h0-y0
			paths.append(2)
		if x < 2:
			h0 = 2+h0
			paths.append(3)
		else:
			h0 = h0-2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h0 = x**0.5
		return h0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))