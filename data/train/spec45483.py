import numpy as np 

def function(x):

	v0 = x
	c9 = x
	paths = []
	try:
		if c9 >= 6:
			c9 = c9-4
			paths.append(1)
		else:
			v0 = v0*v0
			x = v0/x
			paths.append(2)
		if v0 < 9:
			c9 = v0+c9
			x = x/4
			paths.append(3)
		else:
			v0 = 6+v0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c9 = x**0.5
		return c9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))