import numpy as np 

def function(x):

	o9 = 6
	z0 = x
	x = x
	paths = []
	try:
		if z0 <= 8:
			o9 = z0+z0
			x = x/x
			paths.append(1)
		else:
			z0 = 4+x
			paths.append(2)
		if z0 <= 7:
			x = x/z0
			z0 = o9*z0
			paths.append(3)
		else:
			x = 0-9
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