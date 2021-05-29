import numpy as np 

def function(x):

	z8 = 5
	z0 = x
	paths = []
	try:
		if z0 >= 8:
			x = x/5
			paths.append(1)
		else:
			x = x+x
			z0 = z0+z8
			z0 = z0-z8
			paths.append(2)
		if x > 5:
			z0 = z0*z8
			z8 = z8-4
			paths.append(3)
		else:
			z8 = x*1
			z8 = 2-x
			paths.append(4)
		paths.append(5)
		assert z8 >= 0
		z0 = z8**0.5
		return z0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))