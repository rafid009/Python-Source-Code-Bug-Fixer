import numpy as np 

def function(x):

	h5 = 1
	c1 = 0
	paths = []
	try:
		if c1 < 2:
			h5 = 1-0
			c1 = c1+c1
			x = x*1
			paths.append(1)
		else:
			x = 1-x
			paths.append(2)
		if h5 < 0:
			h5 = c1+0
			x = 2-x
			c1 = 2+9
			paths.append(3)
		else:
			c1 = c1*c1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c1 = x**0.5
		return c1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))