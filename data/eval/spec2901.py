import numpy as np 

def function(x):

	c7 = x
	o8 = 6
	paths = []
	try:
		if o8 < 2:
			x = x*o8
			paths.append(1)
		else:
			o8 = 8/o8
			c7 = 1/7
			c7 = o8/7
			paths.append(2)
		if x < 4:
			o8 = o8*4
			paths.append(3)
		else:
			o8 = 2-2
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