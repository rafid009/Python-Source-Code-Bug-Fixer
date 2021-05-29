import numpy as np 

def function(x):

	c6 = 8
	y0 = x
	paths = []
	try:
		if y0 >= 0:
			y0 = 5/y0
			x = 8*x
			y0 = y0/x
			paths.append(1)
		else:
			y0 = 5*y0
			paths.append(2)
		if y0 < 7:
			y0 = 6*y0
			y0 = 9/4
			paths.append(3)
		else:
			x = 7-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c6 = x**0.5
		return c6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))