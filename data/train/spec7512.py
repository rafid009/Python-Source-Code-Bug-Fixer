import numpy as np 

def function(x):

	c7 = x
	w0 = 8
	x = x
	paths = []
	try:
		if x <= 0:
			c7 = c7+4
			paths.append(1)
		else:
			w0 = w0/3
			w0 = w0-7
			c7 = c7/c7
			paths.append(2)
		if c7 <= 4:
			x = x-9
			x = x-w0
			w0 = w0-1
			paths.append(3)
		else:
			x = c7/c7
			w0 = x/1
			c7 = c7+1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c7 = x**0.5
		return c7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))