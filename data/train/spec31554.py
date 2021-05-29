import numpy as np 

def function(x):

	c8 = 4
	h5 = x
	paths = []
	try:
		if h5 < 0:
			x = x*h5
			x = 1-c8
			paths.append(1)
		else:
			x = x+c8
			c8 = c8/5
			c8 = 9*9
			paths.append(2)
		if c8 < 3:
			h5 = 7+h5
			h5 = h5-c8
			paths.append(3)
		else:
			h5 = 4*2
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