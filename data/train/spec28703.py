import numpy as np 

def function(x):

	g1 = x
	c6 = 5
	paths = []
	try:
		if x > 5:
			g1 = c6-x
			paths.append(1)
		else:
			g1 = g1*6
			x = x*4
			c6 = x/c6
			paths.append(2)
		if c6 < 1:
			x = x*x
			paths.append(3)
		else:
			x = x-3
			g1 = g1/x
			paths.append(4)
		paths.append(5)
		assert g1 >= 0
		c6 = g1**0.5
		return c6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))