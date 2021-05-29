import numpy as np 

def function(x):

	c3 = x
	g9 = 5
	x = x
	paths = []
	try:
		if x <= 8:
			g9 = g9+1
			x = 2-x
			paths.append(1)
		else:
			g9 = g9*6
			paths.append(2)
		if c3 < 8:
			g9 = g9/4
			paths.append(3)
		else:
			g9 = g9-3
			x = x-9
			c3 = c3-2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c3 = x**0.5
		return c3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))