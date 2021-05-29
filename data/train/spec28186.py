import numpy as np 

def function(x):

	h5 = x
	g7 = 8
	paths = []
	try:
		if g7 <= 6:
			g7 = g7*h5
			g7 = g7/1
			paths.append(1)
		else:
			h5 = 6*h5
			paths.append(2)
		if g7 >= 6:
			h5 = 2/x
			g7 = 0-x
			paths.append(3)
		else:
			h5 = h5-6
			x = 0-6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g7 = x**0.5
		return g7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))