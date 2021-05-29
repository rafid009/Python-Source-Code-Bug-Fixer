import numpy as np 

def function(x):

	z8 = 3
	z0 = 7
	paths = []
	try:
		if z8 >= 7:
			z8 = 8-8
			paths.append(1)
		else:
			z0 = x*9
			z8 = 7+z8
			paths.append(2)
		if z0 <= 5:
			z8 = z8+x
			paths.append(3)
		else:
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