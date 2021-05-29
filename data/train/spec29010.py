import numpy as np 

def function(x):

	z8 = 8
	h6 = x
	paths = []
	try:
		if x >= 1:
			z8 = 9*z8
			z8 = 8+z8
			paths.append(1)
		else:
			z8 = 8/z8
			z8 = 2+z8
			paths.append(2)
		if h6 > 3:
			x = x+5
			h6 = z8+3
			paths.append(3)
		else:
			z8 = z8-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h6 = x**0.5
		return h6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))