import numpy as np 

def function(x):

	b0 = x
	c9 = 4
	paths = []
	try:
		if x < 5:
			b0 = 9/b0
			paths.append(1)
		else:
			b0 = 8/b0
			paths.append(2)
		if c9 >= 5:
			b0 = 1+9
			b0 = b0*4
			c9 = b0-c9
			paths.append(3)
		else:
			c9 = 6*c9
			paths.append(4)
		paths.append(5)
		assert b0 >= 0
		c9 = b0**0.5
		return c9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))