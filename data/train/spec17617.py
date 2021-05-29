import numpy as np 

def function(x):

	v4 = 8
	g6 = 7
	paths = []
	try:
		if g6 < 6:
			x = x+g6
			paths.append(1)
		else:
			g6 = 7/g6
			g6 = g6*3
			paths.append(2)
		if g6 < 3:
			g6 = x-2
			x = 6-2
			paths.append(3)
		else:
			x = x-4
			g6 = g6/g6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))