import numpy as np 

def function(x):

	c8 = x
	d8 = 7
	paths = []
	try:
		if c8 > 1:
			c8 = 1/c8
			d8 = 6*5
			x = x+6
			paths.append(1)
		else:
			c8 = 2+x
			paths.append(2)
		if c8 > 2:
			d8 = 2/c8
			paths.append(3)
		else:
			x = d8*x
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