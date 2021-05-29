import numpy as np 

def function(x):

	n2 = 6
	z0 = 3
	paths = []
	try:
		if n2 < 0:
			z0 = z0/z0
			z0 = 0/x
			z0 = n2/1
			paths.append(1)
		else:
			x = 0-z0
			z0 = z0-0
			n2 = x*n2
			paths.append(2)
		if x <= 6:
			x = x+3
			z0 = z0*x
			x = 8+x
			paths.append(3)
		else:
			z0 = n2*6
			paths.append(4)
		paths.append(5)
		assert n2 >= 0
		z0 = n2**0.5
		return z0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))