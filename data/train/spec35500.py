import numpy as np 

def function(x):

	c0 = 5
	a4 = 3
	x = x
	paths = []
	try:
		if a4 < 6:
			a4 = a4*c0
			paths.append(1)
		else:
			a4 = a4*6
			a4 = c0-3
			paths.append(2)
		if x > 2:
			x = 9+x
			a4 = a4*6
			c0 = c0/2
			paths.append(3)
		else:
			c0 = c0/c0
			c0 = 6/c0
			c0 = 7*c0
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