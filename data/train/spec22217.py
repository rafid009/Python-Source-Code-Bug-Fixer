import numpy as np 

def function(x):

	c8 = 1
	z7 = x
	paths = []
	try:
		if z7 > 9:
			c8 = z7-c8
			paths.append(1)
		else:
			z7 = 1/z7
			x = 8-8
			paths.append(2)
		if c8 < 2:
			c8 = c8/3
			c8 = 9/c8
			c8 = 3/6
			paths.append(3)
		else:
			c8 = c8-c8
			c8 = z7-2
			c8 = 8/c8
			paths.append(4)
		paths.append(5)
		assert z7 >= 0
		x = z7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))