import numpy as np 

def function(x):

	z0 = 0
	n2 = 2
	paths = []
	try:
		if z0 > 1:
			n2 = n2*1
			n2 = z0/5
			x = z0/x
			paths.append(1)
		else:
			x = 6*x
			n2 = 9+4
			z0 = z0/7
			paths.append(2)
		if z0 < 7:
			z0 = z0-8
			z0 = 0/x
			paths.append(3)
		else:
			x = 0/5
			z0 = z0*n2
			z0 = 4-z0
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