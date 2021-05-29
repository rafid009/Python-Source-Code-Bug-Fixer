import numpy as np 

def function(x):

	c6 = x
	g4 = x
	paths = []
	try:
		if c6 > 8:
			g4 = g4-3
			paths.append(1)
		else:
			c6 = 6/4
			c6 = 7+c6
			x = 8-x
			paths.append(2)
		if x <= 1:
			c6 = c6/9
			c6 = g4*9
			paths.append(3)
		else:
			c6 = x*c6
			paths.append(4)
		paths.append(5)
		assert g4 >= 0
		c6 = g4**0.5
		return c6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))