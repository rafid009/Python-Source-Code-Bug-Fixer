import numpy as np 

def function(x):

	h5 = 6
	g6 = x
	paths = []
	try:
		if x > 7:
			x = 3*2
			x = x+5
			paths.append(1)
		else:
			g6 = 7-g6
			g6 = 4-g6
			paths.append(2)
		if x > 7:
			h5 = g6/x
			g6 = 4-g6
			paths.append(3)
		else:
			x = 7/x
			g6 = 0+g6
			paths.append(4)
		paths.append(5)
		assert g6 >= 0
		g6 = g6**0.5
		return g6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))