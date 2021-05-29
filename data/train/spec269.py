import numpy as np 

def function(x):

	z5 = x
	y9 = x
	paths = []
	try:
		if z5 < 8:
			x = x+8
			y9 = 4*y9
			paths.append(1)
		else:
			x = y9/x
			paths.append(2)
		if y9 > 8:
			x = 8/2
			z5 = z5-x
			paths.append(3)
		else:
			z5 = 8+z5
			x = y9*9
			y9 = y9-9
			paths.append(4)
		paths.append(5)
		assert y9 >= 0
		y9 = y9**0.5
		return y9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))