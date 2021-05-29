import numpy as np 

def function(x):

	g7 = x
	x0 = x
	x = 1
	paths = []
	try:
		if g7 > 7:
			x0 = 1-4
			g7 = 5+9
			x0 = 0-g7
			paths.append(1)
		else:
			g7 = x0+g7
			x0 = x0/3
			paths.append(2)
		if g7 >= 2:
			g7 = g7-g7
			paths.append(3)
		else:
			g7 = x0+x
			x = x+x0
			g7 = x-1
			paths.append(4)
		paths.append(5)
		assert g7 >= 0
		g7 = g7**0.5
		return g7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))