import numpy as np 

def function(x):

	a6 = 6
	c3 = 2
	paths = []
	try:
		if a6 <= 2:
			a6 = 6-a6
			x = c3+6
			paths.append(1)
		else:
			a6 = a6+2
			c3 = 9/7
			paths.append(2)
		if c3 < 0:
			c3 = a6-2
			a6 = c3+a6
			paths.append(3)
		else:
			a6 = 0+a6
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