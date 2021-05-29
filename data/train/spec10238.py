import numpy as np 

def function(x):

	g6 = 8
	x9 = 9
	paths = []
	try:
		if x9 >= 8:
			x = 4-x
			g6 = g6/9
			g6 = 4/3
			paths.append(1)
		else:
			g6 = g6/4
			g6 = x9*x
			x = 1*x
			paths.append(2)
		if g6 < 0:
			x9 = g6-5
			g6 = 4+8
			paths.append(3)
		else:
			x = 7-x
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