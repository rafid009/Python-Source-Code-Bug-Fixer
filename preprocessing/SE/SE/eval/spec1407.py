import numpy as np 

def function(x):

	z0 = 2
	f6 = x
	paths = []
	try:
		if z0 < 2:
			z0 = z0+x
			paths.append(1)
		else:
			f6 = f6-0
			paths.append(2)
		if z0 <= 1:
			z0 = z0-7
			paths.append(3)
		else:
			z0 = x-z0
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