import numpy as np 

def function(x):

	c0 = x
	y9 = 7
	paths = []
	try:
		if x > 6:
			y9 = 1/9
			c0 = 1/c0
			paths.append(1)
		else:
			y9 = 0-y9
			paths.append(2)
		if y9 > 1:
			y9 = y9/x
			x = 1*x
			paths.append(3)
		else:
			y9 = 7*3
			x = c0/y9
			x = x/1
			paths.append(4)
		paths.append(5)
		assert c0 >= 0
		y9 = c0**0.5
		return y9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))