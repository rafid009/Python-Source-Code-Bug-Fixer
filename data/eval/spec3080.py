import numpy as np 

def function(x):

	h5 = x
	w7 = 8
	paths = []
	try:
		if h5 < 0:
			w7 = x+4
			x = x*x
			paths.append(1)
		else:
			h5 = 7+0
			paths.append(2)
		if w7 < 7:
			w7 = w7+0
			h5 = h5*x
			h5 = 9*h5
			paths.append(3)
		else:
			x = x+8
			x = 1-x
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