import numpy as np 

def function(x):

	z0 = x
	h5 = 8
	x = x
	paths = []
	try:
		if z0 <= 1:
			z0 = z0+x
			x = 6/x
			paths.append(1)
		else:
			z0 = z0+8
			z0 = h5+5
			paths.append(2)
		if x >= 8:
			x = 8/8
			paths.append(3)
		else:
			z0 = 1+2
			x = x-7
			h5 = 4*3
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