import numpy as np 

def function(x):

	g0 = 4
	y0 = x
	paths = []
	try:
		if g0 < 2:
			x = 5-x
			g0 = g0+5
			paths.append(1)
		else:
			g0 = 8-g0
			paths.append(2)
		if g0 >= 2:
			x = g0*x
			paths.append(3)
		else:
			g0 = 1/g0
			paths.append(4)
		paths.append(5)
		assert y0 >= 0
		g0 = y0**0.5
		return g0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))