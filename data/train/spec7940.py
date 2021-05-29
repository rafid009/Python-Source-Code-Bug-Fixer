import numpy as np 

def function(x):

	z8 = 8
	o3 = x
	paths = []
	try:
		if z8 <= 2:
			o3 = x+o3
			z8 = x/z8
			z8 = x*z8
			paths.append(1)
		else:
			x = x/9
			z8 = z8*8
			x = 1-z8
			paths.append(2)
		if o3 > 1:
			z8 = z8+6
			paths.append(3)
		else:
			z8 = z8-8
			z8 = 5/2
			z8 = z8-3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o3 = x**0.5
		return o3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))