import numpy as np 

def function(x):

	x1 = 2
	g6 = x
	paths = []
	try:
		if x1 >= 0:
			g6 = 2-x
			x1 = 4-7
			paths.append(1)
		else:
			g6 = g6/2
			paths.append(2)
		if x1 > 9:
			x = 3-x
			x = x-2
			g6 = g6-x1
			paths.append(3)
		else:
			x = x/2
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