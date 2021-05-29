import numpy as np 

def function(x):

	d1 = 1
	c1 = 2
	paths = []
	try:
		if x > 0:
			c1 = c1-c1
			x = 1+d1
			d1 = x+x
			paths.append(1)
		else:
			c1 = 2-c1
			d1 = d1/7
			d1 = x+d1
			paths.append(2)
		if c1 >= 5:
			c1 = 1-c1
			x = 7-d1
			paths.append(3)
		else:
			x = 1-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c1 = x**0.5
		return c1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))