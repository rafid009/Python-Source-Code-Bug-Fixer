import numpy as np 

def function(x):

	c0 = 0
	w2 = 0
	paths = []
	try:
		if x > 2:
			x = 9+x
			c0 = c0*2
			paths.append(1)
		else:
			w2 = 3*2
			paths.append(2)
		if x >= 0:
			c0 = c0-0
			paths.append(3)
		else:
			w2 = c0-w2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c0 = x**0.5
		return c0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))