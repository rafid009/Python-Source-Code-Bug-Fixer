import numpy as np 

def function(x):

	c4 = x
	p0 = x
	paths = []
	try:
		if p0 < 3:
			x = 2*x
			paths.append(1)
		else:
			c4 = 5*4
			paths.append(2)
		if p0 < 1:
			x = x/4
			paths.append(3)
		else:
			p0 = p0-p0
			c4 = 9-9
			paths.append(4)
		paths.append(5)
		assert p0 >= 0
		c4 = p0**0.5
		return c4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))