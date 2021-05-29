import numpy as np 

def function(x):

	c7 = x
	w0 = x
	paths = []
	try:
		if c7 < 4:
			c7 = 2*7
			c7 = c7-5
			paths.append(1)
		else:
			c7 = 6*c7
			paths.append(2)
		if x < 4:
			c7 = 9-c7
			x = x-4
			x = 1-w0
			paths.append(3)
		else:
			c7 = c7-8
			w0 = x*w0
			paths.append(4)
		paths.append(5)
		assert w0 >= 0
		c7 = w0**0.5
		return c7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))