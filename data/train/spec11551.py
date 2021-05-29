import numpy as np 

def function(x):

	z6 = 2
	z8 = x
	x = x
	paths = []
	try:
		if z8 > 0:
			x = 3-8
			z8 = x/z6
			paths.append(1)
		else:
			x = x*x
			x = x*x
			paths.append(2)
		if x >= 9:
			z8 = z8-6
			z8 = z8*5
			z6 = z6/z6
			paths.append(3)
		else:
			x = x/7
			z8 = z8*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z6 = x**0.5
		return z6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))