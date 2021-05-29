import numpy as np 

def function(x):

	c6 = 9
	h5 = 3
	paths = []
	try:
		if x < 1:
			x = x+x
			paths.append(1)
		else:
			x = 5*x
			c6 = x/5
			paths.append(2)
		if h5 < 6:
			c6 = 0-x
			x = x-7
			paths.append(3)
		else:
			h5 = h5-3
			h5 = 4+h5
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