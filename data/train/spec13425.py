import numpy as np 

def function(x):

	k2 = x
	c4 = x
	paths = []
	try:
		if c4 > 2:
			x = x-4
			c4 = 6+c4
			k2 = c4*3
			paths.append(1)
		else:
			x = c4-c4
			x = 6+x
			x = 7-x
			paths.append(2)
		if c4 > 8:
			c4 = c4-9
			k2 = k2*k2
			k2 = 4*k2
			paths.append(3)
		else:
			c4 = 5+c4
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