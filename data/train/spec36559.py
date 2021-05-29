import numpy as np 

def function(x):

	z6 = 4
	z0 = x
	paths = []
	try:
		if x <= 6:
			z0 = z0+3
			z6 = z6/9
			z6 = 1/z6
			paths.append(1)
		else:
			x = 1/x
			z0 = 5-z0
			paths.append(2)
		if z6 > 3:
			z6 = z0*z6
			paths.append(3)
		else:
			z6 = 5+2
			x = x+1
			z0 = z0+9
			paths.append(4)
		paths.append(5)
		assert z0 >= 0
		z0 = z0**0.5
		return z0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))