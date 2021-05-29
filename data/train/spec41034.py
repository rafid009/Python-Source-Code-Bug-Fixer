import numpy as np 

def function(x):

	c8 = x
	r9 = 7
	paths = []
	try:
		if r9 > 1:
			x = 2+x
			c8 = c8/4
			r9 = 9*4
			paths.append(1)
		else:
			c8 = 3-6
			x = 9/5
			paths.append(2)
		if c8 >= 8:
			c8 = c8/4
			x = x+0
			c8 = c8-3
			paths.append(3)
		else:
			r9 = x/r9
			c8 = c8/c8
			x = x*c8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c8 = x**0.5
		return c8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))