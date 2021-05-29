import numpy as np 

def function(x):

	l4 = 0
	h5 = 3
	x = 8
	paths = []
	try:
		if x >= 2:
			h5 = h5-l4
			paths.append(1)
		else:
			x = 2*x
			h5 = l4+h5
			l4 = x*l4
			paths.append(2)
		if h5 > 3:
			x = h5-h5
			h5 = h5-3
			l4 = x*h5
			paths.append(3)
		else:
			x = x+l4
			h5 = x+4
			x = 6-h5
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