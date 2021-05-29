import numpy as np 

def function(x):

	z0 = x
	p8 = x
	paths = []
	try:
		if x >= 5:
			x = x-6
			z0 = 3+z0
			paths.append(1)
		else:
			z0 = z0+p8
			x = x-9
			p8 = 1+p8
			paths.append(2)
		if p8 > 6:
			z0 = 4*z0
			p8 = z0/p8
			paths.append(3)
		else:
			z0 = z0*z0
			p8 = p8+6
			z0 = p8+z0
			paths.append(4)
		paths.append(5)
		assert p8 >= 0
		x = p8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))