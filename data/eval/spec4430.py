import numpy as np 

def function(x):

	c6 = x
	g5 = x
	paths = []
	try:
		if c6 >= 5:
			g5 = 5-6
			g5 = 9+6
			paths.append(1)
		else:
			x = 5*c6
			x = g5/8
			paths.append(2)
		if g5 >= 6:
			c6 = c6*x
			g5 = g5/x
			paths.append(3)
		else:
			c6 = 0*3
			c6 = 6-c6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g5 = x**0.5
		return g5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))