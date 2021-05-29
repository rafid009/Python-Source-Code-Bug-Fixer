import numpy as np 

def function(x):

	y0 = 8
	g9 = 6
	paths = []
	try:
		if y0 > 0:
			y0 = 5-y0
			y0 = 8/y0
			paths.append(1)
		else:
			y0 = 9/y0
			y0 = 7-7
			paths.append(2)
		if y0 > 7:
			x = x*y0
			g9 = g9*5
			paths.append(3)
		else:
			y0 = y0/y0
			x = 3-9
			g9 = y0-2
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