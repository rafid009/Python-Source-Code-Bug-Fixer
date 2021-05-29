import numpy as np 

def function(x):

	z8 = x
	z4 = 0
	paths = []
	try:
		if z8 >= 1:
			z8 = z8+1
			x = x/3
			z4 = z4*z4
			paths.append(1)
		else:
			z4 = z4-6
			z4 = 7-z4
			paths.append(2)
		if z4 < 8:
			z4 = 2*5
			z4 = z4/9
			paths.append(3)
		else:
			x = 9-8
			x = 1/z8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z8 = x**0.5
		return z8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))