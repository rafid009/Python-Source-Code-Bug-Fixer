import numpy as np 

def function(x):

	b8 = x
	c9 = 2
	paths = []
	try:
		if c9 > 7:
			x = x-c9
			paths.append(1)
		else:
			x = x+9
			b8 = c9+0
			paths.append(2)
		if c9 <= 0:
			c9 = 3/c9
			c9 = c9-8
			x = 0/x
			paths.append(3)
		else:
			c9 = x-4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c9 = x**0.5
		return c9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))