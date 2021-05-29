import numpy as np 

def function(x):

	g6 = x
	h5 = 7
	paths = []
	try:
		if g6 < 4:
			h5 = 6-g6
			paths.append(1)
		else:
			h5 = 5/3
			h5 = 7-h5
			paths.append(2)
		if x <= 1:
			h5 = g6*h5
			h5 = h5/g6
			g6 = g6*9
			paths.append(3)
		else:
			g6 = 7-5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g6 = x**0.5
		return g6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))