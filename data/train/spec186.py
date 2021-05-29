import numpy as np 

def function(x):

	c0 = 3
	o8 = x
	paths = []
	try:
		if o8 <= 1:
			c0 = 2+5
			o8 = 7-8
			o8 = x+o8
			paths.append(1)
		else:
			o8 = o8-2
			paths.append(2)
		if o8 < 2:
			x = 3/x
			o8 = o8-6
			c0 = c0-4
			paths.append(3)
		else:
			c0 = 5/c0
			paths.append(4)
		paths.append(5)
		assert o8 >= 0
		c0 = o8**0.5
		return c0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))