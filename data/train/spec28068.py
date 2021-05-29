import numpy as np 

def function(x):

	c8 = 2
	x6 = x
	paths = []
	try:
		if c8 <= 3:
			c8 = c8/3
			c8 = 2/c8
			c8 = x6*c8
			paths.append(1)
		else:
			c8 = c8+9
			c8 = 7/1
			paths.append(2)
		if c8 > 3:
			x6 = x6-4
			paths.append(3)
		else:
			x6 = x6+8
			x6 = 4-x6
			paths.append(4)
		paths.append(5)
		assert x6 >= 0
		c8 = x6**0.5
		return c8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))