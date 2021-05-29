import numpy as np 

def function(x):

	b0 = 1
	z0 = 7
	paths = []
	try:
		if z0 < 8:
			b0 = b0*4
			paths.append(1)
		else:
			b0 = z0-b0
			z0 = b0+z0
			paths.append(2)
		if b0 <= 2:
			z0 = 9*z0
			paths.append(3)
		else:
			b0 = b0-9
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