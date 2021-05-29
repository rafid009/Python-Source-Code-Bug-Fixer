import numpy as np 

def function(x):

	n8 = 1
	c3 = 4
	paths = []
	try:
		if n8 < 3:
			c3 = n8-c3
			paths.append(1)
		else:
			c3 = c3-5
			c3 = 3-c3
			paths.append(2)
		if c3 < 8:
			x = x*c3
			x = x-1
			paths.append(3)
		else:
			n8 = 4-1
			x = c3*x
			n8 = c3*2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c3 = x**0.5
		return c3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))