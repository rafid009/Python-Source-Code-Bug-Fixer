import numpy as np 

def function(x):

	z0 = x
	z1 = 2
	paths = []
	try:
		if x < 6:
			z1 = z1*0
			x = x+7
			z1 = 5*z0
			paths.append(1)
		else:
			x = x-4
			z0 = z0-x
			z1 = 7/z1
			paths.append(2)
		if x <= 5:
			z0 = z0-2
			z1 = 3*z1
			paths.append(3)
		else:
			z0 = 2*z0
			z1 = z1*x
			z0 = 2*z0
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