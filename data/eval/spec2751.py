import numpy as np 

def function(x):

	y9 = x
	c9 = x
	x = 7
	paths = []
	try:
		if c9 > 6:
			c9 = c9+9
			x = x*4
			y9 = y9+y9
			paths.append(1)
		else:
			y9 = c9+7
			y9 = y9-1
			paths.append(2)
		if y9 <= 6:
			x = x+c9
			paths.append(3)
		else:
			c9 = 4*x
			c9 = 0/y9
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