import numpy as np 

def function(x):

	g6 = 6
	y7 = 6
	paths = []
	try:
		if x < 2:
			g6 = y7-3
			y7 = y7/6
			paths.append(1)
		else:
			g6 = 2+g6
			x = 4+y7
			y7 = x-0
			paths.append(2)
		if g6 >= 9:
			x = 1-1
			g6 = 9-g6
			y7 = y7*4
			paths.append(3)
		else:
			g6 = g6*7
			y7 = y7+y7
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