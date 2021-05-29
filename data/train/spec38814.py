import numpy as np 

def function(x):

	g6 = 4
	n6 = x
	paths = []
	try:
		if g6 <= 2:
			g6 = g6*6
			paths.append(1)
		else:
			g6 = n6-x
			x = 5-x
			paths.append(2)
		if n6 < 3:
			g6 = g6-g6
			x = 3/x
			paths.append(3)
		else:
			n6 = x/3
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