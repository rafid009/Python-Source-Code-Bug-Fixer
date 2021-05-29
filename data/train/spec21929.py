import numpy as np 

def function(x):

	n9 = 5
	z8 = 9
	paths = []
	try:
		if n9 > 2:
			z8 = 1*7
			z8 = 5+z8
			paths.append(1)
		else:
			z8 = x-n9
			paths.append(2)
		if n9 > 8:
			z8 = 9-z8
			paths.append(3)
		else:
			z8 = 5+z8
			x = 0-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n9 = x**0.5
		return n9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))