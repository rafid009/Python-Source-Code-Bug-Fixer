import numpy as np 

def function(x):

	z8 = 9
	v0 = x
	paths = []
	try:
		if z8 < 5:
			x = 8/7
			paths.append(1)
		else:
			z8 = 4+4
			z8 = v0-7
			paths.append(2)
		if z8 < 9:
			z8 = z8+4
			x = 9+v0
			z8 = x-z8
			paths.append(3)
		else:
			v0 = v0*z8
			x = z8*2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z8 = x**0.5
		return z8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))