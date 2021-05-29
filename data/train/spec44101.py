import numpy as np 

def function(x):

	y9 = x
	z8 = x
	x = 5
	paths = []
	try:
		if y9 > 2:
			x = y9+x
			y9 = y9+z8
			paths.append(1)
		else:
			z8 = 5+z8
			y9 = x*y9
			x = z8+2
			paths.append(2)
		if z8 >= 6:
			y9 = y9+x
			paths.append(3)
		else:
			z8 = z8+y9
			x = 8+x
			paths.append(4)
		paths.append(5)
		assert y9 >= 0
		z8 = y9**0.5
		return z8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))