import numpy as np 

def function(x):

	c5 = x
	y4 = 4
	paths = []
	try:
		if c5 > 3:
			y4 = 4+y4
			paths.append(1)
		else:
			x = x-6
			y4 = y4+c5
			paths.append(2)
		if c5 <= 3:
			c5 = 4*c5
			paths.append(3)
		else:
			c5 = c5*c5
			c5 = c5-7
			paths.append(4)
		paths.append(5)
		assert y4 >= 0
		c5 = y4**0.5
		return c5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))