import numpy as np 

def function(x):

	g7 = 1
	e6 = 2
	paths = []
	try:
		if e6 < 3:
			g7 = 0-8
			g7 = g7-e6
			g7 = g7+g7
			paths.append(1)
		else:
			g7 = g7/g7
			paths.append(2)
		if x >= 9:
			g7 = g7-8
			x = 3-e6
			g7 = 9/e6
			paths.append(3)
		else:
			e6 = g7+g7
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