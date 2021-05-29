import numpy as np 

def function(x):

	h0 = x
	z0 = 0
	paths = []
	try:
		if x >= 8:
			h0 = h0+2
			x = x/2
			paths.append(1)
		else:
			z0 = h0-z0
			h0 = h0+3
			paths.append(2)
		if z0 <= 7:
			x = z0+2
			z0 = z0+z0
			z0 = z0*5
			paths.append(3)
		else:
			z0 = z0*x
			z0 = x+3
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