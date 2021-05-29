import numpy as np 

def function(x):

	v5 = x
	c0 = x
	paths = []
	try:
		if v5 > 8:
			x = x*x
			c0 = 2-c0
			v5 = c0/v5
			paths.append(1)
		else:
			x = x*x
			paths.append(2)
		if v5 <= 4:
			x = 3-x
			paths.append(3)
		else:
			c0 = 8-c0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c0 = x**0.5
		return c0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))