import numpy as np 

def function(x):

	k0 = 5
	c4 = 9
	x = x
	paths = []
	try:
		if c4 < 8:
			x = x-x
			paths.append(1)
		else:
			k0 = 4*2
			paths.append(2)
		if k0 >= 7:
			c4 = c4*c4
			x = 4/x
			k0 = k0/k0
			paths.append(3)
		else:
			x = 7-x
			k0 = k0-5
			c4 = c4+7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c4 = x**0.5
		return c4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))