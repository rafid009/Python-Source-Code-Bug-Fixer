import numpy as np 

def function(x):

	z8 = 3
	e7 = 4
	paths = []
	try:
		if x > 0:
			z8 = 7*z8
			z8 = z8*z8
			paths.append(1)
		else:
			z8 = x*z8
			z8 = z8+x
			paths.append(2)
		if z8 < 5:
			z8 = 4-z8
			paths.append(3)
		else:
			e7 = x-x
			e7 = 3/3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e7 = x**0.5
		return e7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))