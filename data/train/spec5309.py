import numpy as np 

def function(x):

	d8 = 3
	c2 = 7
	paths = []
	try:
		if x > 7:
			c2 = x-c2
			paths.append(1)
		else:
			c2 = 2/9
			d8 = 5/d8
			paths.append(2)
		if x >= 8:
			x = x-0
			paths.append(3)
		else:
			c2 = d8/c2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c2 = x**0.5
		return c2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))