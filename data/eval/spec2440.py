import numpy as np 

def function(x):

	z4 = 1
	y9 = x
	paths = []
	try:
		if x <= 4:
			x = 4*6
			x = x*y9
			paths.append(1)
		else:
			z4 = x+z4
			z4 = z4*7
			y9 = 7+8
			paths.append(2)
		if z4 <= 2:
			z4 = y9+x
			y9 = 3*1
			y9 = 2-z4
			paths.append(3)
		else:
			y9 = y9*y9
			y9 = 1*y9
			x = 8+x
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