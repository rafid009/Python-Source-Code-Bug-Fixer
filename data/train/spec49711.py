import numpy as np 

def function(x):

	z0 = x
	o8 = 5
	paths = []
	try:
		if z0 > 1:
			x = 0-9
			paths.append(1)
		else:
			z0 = 7/z0
			x = x-8
			paths.append(2)
		if z0 < 8:
			z0 = 4/z0
			paths.append(3)
		else:
			o8 = o8+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o8 = x**0.5
		return o8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))