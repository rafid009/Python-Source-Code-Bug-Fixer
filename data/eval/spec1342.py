import numpy as np 

def function(x):

	o4 = 9
	h1 = 6
	paths = []
	try:
		if h1 < 6:
			o4 = o4+4
			h1 = h1*x
			o4 = o4/o4
			paths.append(1)
		else:
			h1 = h1/8
			h1 = 4*h1
			paths.append(2)
		if h1 < 0:
			h1 = h1*h1
			h1 = o4+3
			paths.append(3)
		else:
			h1 = h1-h1
			x = 2/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h1 = x**0.5
		return h1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))