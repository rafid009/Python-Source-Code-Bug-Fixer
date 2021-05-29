import numpy as np 

def function(x):

	v1 = x
	z0 = 9
	paths = []
	try:
		if x < 5:
			z0 = 7/z0
			paths.append(1)
		else:
			z0 = z0+x
			x = v1-z0
			z0 = x*x
			paths.append(2)
		if x < 4:
			v1 = v1-0
			z0 = 9+8
			z0 = z0*2
			paths.append(3)
		else:
			v1 = 3/v1
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