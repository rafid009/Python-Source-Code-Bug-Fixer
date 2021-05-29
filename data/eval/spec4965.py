import numpy as np 

def function(x):

	z8 = 8
	y9 = 8
	paths = []
	try:
		if x < 4:
			x = x-1
			z8 = z8/6
			y9 = z8/9
			paths.append(1)
		else:
			x = x-8
			paths.append(2)
		if x < 6:
			x = 2+x
			x = 2+x
			paths.append(3)
		else:
			x = z8*x
			y9 = y9/6
			x = y9*9
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