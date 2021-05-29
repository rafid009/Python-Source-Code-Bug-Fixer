import numpy as np 

def function(x):

	z1 = x
	y9 = x
	x = 9
	paths = []
	try:
		if x > 1:
			z1 = 1*z1
			paths.append(1)
		else:
			y9 = 9/z1
			x = x+9
			paths.append(2)
		if y9 < 3:
			y9 = y9*2
			z1 = 3*z1
			x = 8*z1
			paths.append(3)
		else:
			z1 = z1-y9
			x = x*x
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