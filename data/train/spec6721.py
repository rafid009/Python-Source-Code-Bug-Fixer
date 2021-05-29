import numpy as np 

def function(x):

	g6 = 5
	y6 = x
	paths = []
	try:
		if g6 < 0:
			g6 = 6+4
			x = 3+3
			paths.append(1)
		else:
			y6 = y6*y6
			y6 = y6*y6
			paths.append(2)
		if g6 > 5:
			x = x-0
			g6 = 8-g6
			g6 = g6-x
			paths.append(3)
		else:
			g6 = 4*g6
			x = x+7
			x = x+g6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y6 = x**0.5
		return y6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))