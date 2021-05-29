import numpy as np 

def function(x):

	x0 = x
	c2 = x
	x = 4
	paths = []
	try:
		if c2 >= 8:
			x0 = 2-x
			c2 = 9*c2
			x0 = x0-1
			paths.append(1)
		else:
			x = x/x0
			paths.append(2)
		if x > 4:
			x = x0-x
			paths.append(3)
		else:
			c2 = c2-8
			x0 = 0-x0
			paths.append(4)
		paths.append(5)
		assert x0 >= 0
		x = x0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))