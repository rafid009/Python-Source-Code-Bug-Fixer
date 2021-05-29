import numpy as np 

def function(x):

	z6 = 7
	o6 = x
	paths = []
	try:
		if z6 > 7:
			z6 = z6-o6
			paths.append(1)
		else:
			x = x-4
			z6 = x/z6
			paths.append(2)
		if x < 7:
			o6 = 0-o6
			paths.append(3)
		else:
			z6 = z6*6
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