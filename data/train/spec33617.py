import numpy as np 

def function(x):

	c0 = x
	y9 = 5
	paths = []
	try:
		if y9 >= 4:
			x = x*9
			x = c0-c0
			paths.append(1)
		else:
			c0 = y9/x
			c0 = c0+3
			y9 = y9-9
			paths.append(2)
		if c0 > 5:
			x = x-9
			x = x-x
			x = 6/8
			paths.append(3)
		else:
			c0 = c0+1
			paths.append(4)
		paths.append(5)
		assert c0 >= 0
		x = c0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))