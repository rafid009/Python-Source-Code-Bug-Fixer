import numpy as np 

def function(x):

	v3 = 0
	c0 = x
	paths = []
	try:
		if c0 > 6:
			x = v3-3
			paths.append(1)
		else:
			v3 = v3-4
			v3 = 9-c0
			paths.append(2)
		if x >= 4:
			v3 = v3/2
			c0 = c0-x
			paths.append(3)
		else:
			c0 = 8/c0
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