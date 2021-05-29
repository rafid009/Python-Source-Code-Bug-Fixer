import numpy as np 

def function(x):

	d1 = 6
	c3 = 1
	paths = []
	try:
		if x > 1:
			c3 = c3+8
			d1 = d1*7
			paths.append(1)
		else:
			d1 = x*d1
			paths.append(2)
		if d1 < 6:
			x = 0-8
			x = 6-c3
			paths.append(3)
		else:
			x = x-8
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