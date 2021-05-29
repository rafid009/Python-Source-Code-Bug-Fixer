import numpy as np 

def function(x):

	d2 = 5
	c0 = x
	paths = []
	try:
		if c0 >= 5:
			c0 = c0*6
			paths.append(1)
		else:
			d2 = 4/d2
			d2 = x+4
			c0 = c0-8
			paths.append(2)
		if x <= 6:
			c0 = 5*2
			x = x-6
			paths.append(3)
		else:
			d2 = d2+x
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