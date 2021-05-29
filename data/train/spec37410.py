import numpy as np 

def function(x):

	e4 = x
	c0 = x
	paths = []
	try:
		if c0 >= 9:
			x = 5*3
			c0 = c0*c0
			x = 7+x
			paths.append(1)
		else:
			c0 = 4+4
			c0 = 5/c0
			paths.append(2)
		if x <= 5:
			x = 3-1
			e4 = e4+e4
			paths.append(3)
		else:
			c0 = 8/3
			c0 = c0/e4
			paths.append(4)
		paths.append(5)
		assert e4 >= 0
		c0 = e4**0.5
		return c0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))