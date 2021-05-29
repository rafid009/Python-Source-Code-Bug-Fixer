import numpy as np 

def function(x):

	g7 = x
	g6 = 6
	paths = []
	try:
		if x <= 8:
			g6 = g6*8
			paths.append(1)
		else:
			g7 = g6*g7
			x = g7+8
			g6 = 5*x
			paths.append(2)
		if x >= 7:
			g7 = x-8
			x = x/g7
			g7 = 9+g7
			paths.append(3)
		else:
			x = x+1
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