import numpy as np 

def function(x):

	g7 = x
	y3 = 6
	paths = []
	try:
		if g7 >= 3:
			y3 = 1/x
			paths.append(1)
		else:
			g7 = g7*9
			g7 = 8/g7
			y3 = 8-y3
			paths.append(2)
		if y3 > 5:
			g7 = g7/y3
			g7 = g7*9
			paths.append(3)
		else:
			x = x/2
			g7 = 7*g7
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