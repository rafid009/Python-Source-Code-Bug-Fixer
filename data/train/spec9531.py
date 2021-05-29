import numpy as np 

def function(x):

	g7 = 0
	c2 = 5
	paths = []
	try:
		if g7 < 8:
			g7 = g7*7
			paths.append(1)
		else:
			c2 = c2+2
			c2 = 9*c2
			paths.append(2)
		if c2 > 7:
			x = x+c2
			paths.append(3)
		else:
			g7 = c2*g7
			g7 = 5*c2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c2 = x**0.5
		return c2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))