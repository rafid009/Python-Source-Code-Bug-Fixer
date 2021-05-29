import numpy as np 

def function(x):

	y9 = x
	c5 = x
	paths = []
	try:
		if x >= 6:
			c5 = c5-5
			x = x/1
			y9 = y9/8
			paths.append(1)
		else:
			c5 = c5-6
			paths.append(2)
		if c5 >= 5:
			x = x*7
			y9 = 8+c5
			y9 = y9+y9
			paths.append(3)
		else:
			y9 = y9*9
			paths.append(4)
		paths.append(5)
		assert y9 >= 0
		x = y9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))