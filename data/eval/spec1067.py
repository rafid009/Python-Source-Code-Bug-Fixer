import numpy as np 

def function(x):

	c4 = x
	y9 = 1
	paths = []
	try:
		if x < 3:
			y9 = 4*c4
			c4 = 6/y9
			y9 = y9-x
			paths.append(1)
		else:
			c4 = c4-9
			paths.append(2)
		if c4 < 5:
			c4 = 5*c4
			paths.append(3)
		else:
			y9 = y9*x
			c4 = c4*6
			paths.append(4)
		paths.append(5)
		assert c4 >= 0
		y9 = c4**0.5
		return y9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))