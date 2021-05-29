import numpy as np 

def function(x):

	h2 = x
	c0 = x
	paths = []
	try:
		if h2 >= 1:
			c0 = 7/c0
			c0 = 1-c0
			h2 = 6-c0
			paths.append(1)
		else:
			c0 = x-6
			h2 = h2/3
			x = 4/8
			paths.append(2)
		if h2 <= 2:
			x = 9-x
			c0 = 6+8
			paths.append(3)
		else:
			h2 = h2/h2
			x = h2-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))