import numpy as np 

def function(x):

	y9 = x
	z0 = x
	paths = []
	try:
		if x <= 6:
			y9 = y9/y9
			x = x/8
			x = x-8
			paths.append(1)
		else:
			y9 = y9*z0
			x = y9+x
			paths.append(2)
		if x < 1:
			z0 = z0/5
			x = 6+x
			y9 = 8+z0
			paths.append(3)
		else:
			z0 = x*z0
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