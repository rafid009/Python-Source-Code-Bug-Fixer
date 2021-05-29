import numpy as np 

def function(x):

	c8 = 4
	o0 = x
	paths = []
	try:
		if x < 0:
			c8 = o0/c8
			c8 = 9-6
			paths.append(1)
		else:
			o0 = 9+o0
			c8 = c8+7
			paths.append(2)
		if x >= 4:
			c8 = 1-5
			paths.append(3)
		else:
			x = o0-c8
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