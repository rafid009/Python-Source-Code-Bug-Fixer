import numpy as np 

def function(x):

	c9 = x
	d0 = 8
	paths = []
	try:
		if x > 0:
			d0 = d0-d0
			d0 = 5-6
			paths.append(1)
		else:
			d0 = x/d0
			c9 = c9/x
			paths.append(2)
		if c9 < 2:
			c9 = 3+c9
			x = x/1
			d0 = x-d0
			paths.append(3)
		else:
			c9 = x+c9
			c9 = c9/6
			paths.append(4)
		paths.append(5)
		assert d0 >= 0
		c9 = d0**0.5
		return c9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))