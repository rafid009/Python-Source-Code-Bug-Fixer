import numpy as np 

def function(x):

	w4 = x
	c4 = 5
	paths = []
	try:
		if x >= 5:
			w4 = w4*c4
			w4 = w4-w4
			paths.append(1)
		else:
			c4 = x+c4
			x = x-8
			paths.append(2)
		if c4 >= 1:
			w4 = 8-w4
			paths.append(3)
		else:
			c4 = x+w4
			paths.append(4)
		paths.append(5)
		assert w4 >= 0
		c4 = w4**0.5
		return c4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))