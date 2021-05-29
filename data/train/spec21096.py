import numpy as np 

def function(x):

	c1 = x
	g7 = 4
	paths = []
	try:
		if x > 4:
			x = x-7
			paths.append(1)
		else:
			c1 = x-3
			paths.append(2)
		if c1 <= 5:
			g7 = 2*g7
			x = g7*8
			x = 5+x
			paths.append(3)
		else:
			x = g7-6
			g7 = g7+3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c1 = x**0.5
		return c1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))