import numpy as np 

def function(x):

	i7 = 7
	z0 = 5
	paths = []
	try:
		if z0 < 9:
			i7 = x/1
			paths.append(1)
		else:
			z0 = 3*z0
			z0 = i7/2
			z0 = i7*z0
			paths.append(2)
		if z0 < 2:
			z0 = 0-0
			paths.append(3)
		else:
			z0 = 3*i7
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