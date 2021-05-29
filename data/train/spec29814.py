import numpy as np 

def function(x):

	g0 = x
	c7 = x
	paths = []
	try:
		if x > 5:
			x = 8/x
			x = g0-2
			paths.append(1)
		else:
			g0 = 9*c7
			x = c7/4
			g0 = x+8
			paths.append(2)
		if g0 <= 8:
			g0 = 1/g0
			g0 = g0*g0
			paths.append(3)
		else:
			c7 = 8-c7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c7 = x**0.5
		return c7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))