import numpy as np 

def function(x):

	e3 = 8
	c0 = x
	paths = []
	try:
		if x <= 6:
			e3 = c0+e3
			e3 = 7*8
			e3 = e3-6
			paths.append(1)
		else:
			e3 = 2*e3
			paths.append(2)
		if x >= 4:
			x = x*5
			e3 = e3/x
			x = e3/e3
			paths.append(3)
		else:
			c0 = 0/c0
			x = 3/x
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