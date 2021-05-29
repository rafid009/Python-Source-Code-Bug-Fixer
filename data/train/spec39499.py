import numpy as np 

def function(x):

	c9 = x
	d4 = x
	x = 8
	paths = []
	try:
		if x < 0:
			x = x*c9
			c9 = c9/x
			paths.append(1)
		else:
			d4 = 2+d4
			x = 2+x
			paths.append(2)
		if x >= 0:
			c9 = c9-2
			c9 = 0+d4
			x = 9+x
			paths.append(3)
		else:
			x = x/3
			paths.append(4)
		paths.append(5)
		assert d4 >= 0
		c9 = d4**0.5
		return c9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))