import numpy as np 

def function(x):

	z2 = 9
	y9 = x
	paths = []
	try:
		if y9 >= 8:
			y9 = 1*7
			y9 = 4/x
			z2 = z2+x
			paths.append(1)
		else:
			x = x*7
			z2 = z2-3
			paths.append(2)
		if y9 > 4:
			y9 = z2-y9
			paths.append(3)
		else:
			y9 = y9*3
			y9 = 8/y9
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