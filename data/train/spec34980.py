import numpy as np 

def function(x):

	h3 = 9
	c8 = x
	x = 4
	paths = []
	try:
		if c8 >= 1:
			x = x-x
			paths.append(1)
		else:
			c8 = 1-c8
			paths.append(2)
		if c8 > 5:
			x = 4-5
			h3 = h3/x
			paths.append(3)
		else:
			c8 = 0+c8
			x = x-0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h3 = x**0.5
		return h3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))