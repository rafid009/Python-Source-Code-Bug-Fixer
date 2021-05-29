import numpy as np 

def function(x):

	z0 = 4
	d2 = x
	paths = []
	try:
		if x < 1:
			d2 = x/d2
			d2 = 6+6
			d2 = d2-9
			paths.append(1)
		else:
			d2 = x-9
			paths.append(2)
		if x <= 1:
			z0 = 2+z0
			z0 = d2-9
			paths.append(3)
		else:
			d2 = 0/d2
			z0 = z0/x
			x = 7/z0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z0 = x**0.5
		return z0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))