import numpy as np 

def function(x):

	y9 = x
	c1 = 0
	paths = []
	try:
		if x > 3:
			x = 2+x
			c1 = c1*7
			paths.append(1)
		else:
			c1 = 7*1
			paths.append(2)
		if c1 < 6:
			c1 = 2+7
			paths.append(3)
		else:
			y9 = 0*y9
			c1 = x-c1
			x = 3/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y9 = x**0.5
		return y9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))