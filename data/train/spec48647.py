import numpy as np 

def function(x):

	c0 = 8
	o8 = x
	paths = []
	try:
		if x <= 1:
			x = 1/x
			o8 = o8*0
			c0 = c0-0
			paths.append(1)
		else:
			o8 = 5+o8
			paths.append(2)
		if o8 <= 8:
			o8 = o8/4
			c0 = c0*c0
			paths.append(3)
		else:
			x = x-5
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