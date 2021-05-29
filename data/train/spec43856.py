import numpy as np 

def function(x):

	c9 = 9
	w6 = x
	paths = []
	try:
		if x <= 6:
			w6 = w6-3
			paths.append(1)
		else:
			c9 = 2/x
			x = 0*x
			paths.append(2)
		if x > 2:
			c9 = 8*6
			paths.append(3)
		else:
			w6 = c9*w6
			w6 = c9+w6
			w6 = w6-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c9 = x**0.5
		return c9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))