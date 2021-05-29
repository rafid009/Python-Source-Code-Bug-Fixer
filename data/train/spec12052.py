import numpy as np 

def function(x):

	g0 = 5
	c9 = x
	x = x
	paths = []
	try:
		if x >= 1:
			c9 = c9*x
			x = x/2
			paths.append(1)
		else:
			g0 = g0/6
			g0 = x/7
			paths.append(2)
		if c9 > 4:
			g0 = 5-g0
			paths.append(3)
		else:
			g0 = c9+g0
			paths.append(4)
		paths.append(5)
		assert g0 >= 0
		g0 = g0**0.5
		return g0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))