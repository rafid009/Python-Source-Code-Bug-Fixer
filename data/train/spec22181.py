import numpy as np 

def function(x):

	y6 = x
	c9 = x
	paths = []
	try:
		if c9 > 2:
			x = 0/x
			paths.append(1)
		else:
			y6 = 8/y6
			c9 = y6+3
			paths.append(2)
		if x >= 9:
			x = 2-6
			paths.append(3)
		else:
			c9 = c9+0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y6 = x**0.5
		return y6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))