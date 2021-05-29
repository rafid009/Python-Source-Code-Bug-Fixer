import numpy as np 

def function(x):

	y9 = 6
	c1 = 9
	paths = []
	try:
		if y9 <= 7:
			y9 = c1+x
			x = y9/x
			paths.append(1)
		else:
			y9 = y9*c1
			c1 = 3-8
			paths.append(2)
		if y9 <= 9:
			x = 1-x
			x = y9*x
			c1 = 1-8
			paths.append(3)
		else:
			y9 = y9+7
			x = 4-x
			paths.append(4)
		paths.append(5)
		assert c1 >= 0
		c1 = c1**0.5
		return c1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))