import numpy as np 

def function(x):

	g5 = 5
	h5 = x
	paths = []
	try:
		if g5 >= 0:
			g5 = 8-g5
			h5 = h5+6
			paths.append(1)
		else:
			g5 = g5+7
			x = h5/6
			paths.append(2)
		if h5 <= 3:
			x = g5+x
			x = g5-x
			paths.append(3)
		else:
			h5 = 3+8
			x = x/3
			g5 = 9+g5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g5 = x**0.5
		return g5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))