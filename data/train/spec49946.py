import numpy as np 

def function(x):

	c3 = 1
	q9 = 2
	paths = []
	try:
		if c3 < 3:
			c3 = 9/x
			x = c3+x
			paths.append(1)
		else:
			x = x/2
			x = x*q9
			x = 8/c3
			paths.append(2)
		if c3 < 4:
			c3 = c3+6
			paths.append(3)
		else:
			q9 = q9*c3
			x = x-x
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