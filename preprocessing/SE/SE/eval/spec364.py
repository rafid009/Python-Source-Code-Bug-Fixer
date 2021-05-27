import numpy as np 

def function(x):

	y8 = 3
	c8 = x
	paths = []
	try:
		if c8 <= 2:
			y8 = y8-x
			paths.append(1)
		else:
			x = y8/4
			x = c8*x
			paths.append(2)
		if c8 <= 1:
			x = 0-3
			paths.append(3)
		else:
			x = x/8
			c8 = 6*c8
			x = 2*2
			paths.append(4)
		paths.append(5)
		assert c8 >= 0
		c8 = c8**0.5
		return c8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))