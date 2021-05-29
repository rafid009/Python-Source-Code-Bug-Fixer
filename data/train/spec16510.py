import numpy as np 

def function(x):

	c5 = 6
	n0 = 9
	paths = []
	try:
		if n0 > 4:
			n0 = c5*6
			n0 = n0/n0
			c5 = c5/6
			paths.append(1)
		else:
			c5 = 6/c5
			x = 3/9
			x = x+4
			paths.append(2)
		if n0 < 7:
			x = n0-2
			c5 = 8+n0
			x = x*2
			paths.append(3)
		else:
			x = 3/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c5 = x**0.5
		return c5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))