import numpy as np 

def function(x):

	x0 = 4
	c5 = 6
	paths = []
	try:
		if x <= 4:
			c5 = c5/c5
			x = c5/x
			x0 = c5*x0
			paths.append(1)
		else:
			x = 3/6
			x0 = x*9
			paths.append(2)
		if c5 > 7:
			x0 = x0/x
			paths.append(3)
		else:
			x0 = x0+9
			x0 = x0/c5
			c5 = c5+6
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