import numpy as np 

def function(x):

	g6 = x
	x8 = x
	paths = []
	try:
		if g6 >= 1:
			x8 = 8*9
			g6 = g6+8
			paths.append(1)
		else:
			x8 = x8*9
			g6 = g6/6
			paths.append(2)
		if g6 < 7:
			x8 = 3*x8
			x8 = 7-x8
			g6 = 1/g6
			paths.append(3)
		else:
			g6 = g6+4
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