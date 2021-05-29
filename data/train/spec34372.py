import numpy as np 

def function(x):

	g1 = 6
	g6 = x
	paths = []
	try:
		if g6 > 4:
			g1 = 8*g6
			g6 = 8-g6
			paths.append(1)
		else:
			x = 1*x
			x = 4+x
			paths.append(2)
		if g1 >= 8:
			g6 = g6/x
			paths.append(3)
		else:
			g6 = g6+7
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