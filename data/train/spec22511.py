import numpy as np 

def function(x):

	c0 = 1
	g8 = 5
	paths = []
	try:
		if c0 < 1:
			c0 = 6-c0
			g8 = 4*x
			paths.append(1)
		else:
			x = x*9
			paths.append(2)
		if x < 4:
			c0 = 9/x
			g8 = 2+6
			paths.append(3)
		else:
			c0 = 7-c0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g8 = x**0.5
		return g8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))