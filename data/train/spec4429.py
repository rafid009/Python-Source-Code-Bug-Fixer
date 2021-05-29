import numpy as np 

def function(x):

	c1 = 9
	x8 = x
	paths = []
	try:
		if x8 < 0:
			x = c1/x
			x8 = x8/x8
			paths.append(1)
		else:
			x8 = c1/x
			x = x-7
			paths.append(2)
		if c1 <= 0:
			x8 = x8-3
			c1 = 0+5
			c1 = c1-x8
			paths.append(3)
		else:
			x8 = x8-9
			c1 = 5/c1
			c1 = 8/9
			paths.append(4)
		paths.append(5)
		assert x8 >= 0
		c1 = x8**0.5
		return c1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))