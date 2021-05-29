import numpy as np 

def function(x):

	c4 = x
	n0 = 5
	paths = []
	try:
		if n0 > 3:
			c4 = 7*c4
			paths.append(1)
		else:
			n0 = 5+n0
			x = x-5
			paths.append(2)
		if c4 < 2:
			n0 = x/c4
			n0 = n0+4
			c4 = 2-2
			paths.append(3)
		else:
			n0 = n0-9
			n0 = n0-c4
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