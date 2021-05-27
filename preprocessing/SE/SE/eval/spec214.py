import numpy as np 

def function(x):

	v0 = x
	c9 = x
	paths = []
	try:
		if c9 < 5:
			c9 = c9+8
			paths.append(1)
		else:
			c9 = 7+c9
			c9 = c9-3
			v0 = v0/2
			paths.append(2)
		if x >= 5:
			c9 = v0/c9
			x = 8+v0
			v0 = 6/7
			paths.append(3)
		else:
			v0 = 0/v0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v0 = x**0.5
		return v0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))