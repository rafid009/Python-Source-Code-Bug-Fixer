import numpy as np 

def function(x):

	d4 = 8
	c6 = x
	paths = []
	try:
		if c6 > 5:
			c6 = c6/c6
			d4 = c6/d4
			paths.append(1)
		else:
			d4 = d4/c6
			d4 = d4/7
			x = 2+d4
			paths.append(2)
		if c6 > 6:
			d4 = d4-6
			d4 = 0*x
			d4 = x/d4
			paths.append(3)
		else:
			c6 = 1*c6
			x = x/x
			c6 = 7/2
			paths.append(4)
		paths.append(5)
		assert d4 >= 0
		c6 = d4**0.5
		return c6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))