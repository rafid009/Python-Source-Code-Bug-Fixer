import numpy as np 

def function(x):

	g6 = x
	v9 = x
	paths = []
	try:
		if g6 > 4:
			x = 8-x
			paths.append(1)
		else:
			x = v9*x
			paths.append(2)
		if g6 >= 2:
			x = 1-x
			v9 = v9/8
			paths.append(3)
		else:
			v9 = v9*7
			g6 = g6*3
			x = 8*x
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