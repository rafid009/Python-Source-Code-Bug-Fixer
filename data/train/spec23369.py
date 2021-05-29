import numpy as np 

def function(x):

	y9 = x
	z4 = 4
	paths = []
	try:
		if z4 >= 2:
			y9 = 3/y9
			paths.append(1)
		else:
			z4 = 0-z4
			z4 = y9-z4
			x = 5*x
			paths.append(2)
		if y9 > 1:
			y9 = 3+y9
			paths.append(3)
		else:
			z4 = 6-z4
			x = x/5
			z4 = y9-1
			paths.append(4)
		paths.append(5)
		assert z4 >= 0
		y9 = z4**0.5
		return y9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))