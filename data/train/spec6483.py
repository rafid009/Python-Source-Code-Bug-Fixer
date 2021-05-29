import numpy as np 

def function(x):

	z2 = 3
	y9 = x
	paths = []
	try:
		if x <= 5:
			y9 = 3*y9
			z2 = 2+4
			z2 = 5-z2
			paths.append(1)
		else:
			y9 = y9+z2
			y9 = y9*y9
			z2 = z2*4
			paths.append(2)
		if y9 <= 6:
			z2 = z2+8
			z2 = z2+y9
			paths.append(3)
		else:
			x = 7/y9
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