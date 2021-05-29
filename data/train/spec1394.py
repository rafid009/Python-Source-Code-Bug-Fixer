import numpy as np 

def function(x):

	b0 = x
	c8 = 3
	paths = []
	try:
		if x >= 5:
			c8 = c8-2
			x = 1-6
			x = x-3
			paths.append(1)
		else:
			x = b0*x
			b0 = b0*x
			x = x/1
			paths.append(2)
		if b0 < 7:
			c8 = c8*1
			paths.append(3)
		else:
			b0 = 2/1
			paths.append(4)
		paths.append(5)
		assert b0 >= 0
		c8 = b0**0.5
		return c8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))