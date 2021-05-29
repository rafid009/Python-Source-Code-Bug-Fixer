import numpy as np 

def function(x):

	c3 = x
	v5 = 2
	paths = []
	try:
		if c3 < 3:
			c3 = 5*c3
			paths.append(1)
		else:
			c3 = c3+c3
			paths.append(2)
		if c3 <= 6:
			c3 = 0*c3
			paths.append(3)
		else:
			c3 = 5*1
			x = 6-x
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