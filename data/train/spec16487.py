import numpy as np 

def function(x):

	x7 = x
	h5 = x
	paths = []
	try:
		if h5 <= 8:
			h5 = h5/4
			paths.append(1)
		else:
			x7 = x7+1
			h5 = 4-h5
			paths.append(2)
		if x >= 8:
			x7 = x+0
			x7 = 7+1
			paths.append(3)
		else:
			h5 = h5-x
			x7 = h5/x7
			h5 = h5+h5
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