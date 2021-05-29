import numpy as np 

def function(x):

	c0 = 1
	e7 = x
	paths = []
	try:
		if c0 > 6:
			c0 = 0-c0
			x = c0*x
			paths.append(1)
		else:
			c0 = 2-7
			e7 = c0*7
			paths.append(2)
		if x <= 4:
			e7 = 9*e7
			paths.append(3)
		else:
			x = x/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))