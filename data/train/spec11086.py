import numpy as np 

def function(x):

	z8 = x
	d8 = x
	paths = []
	try:
		if d8 >= 6:
			z8 = z8/d8
			paths.append(1)
		else:
			x = 9-x
			z8 = z8+6
			paths.append(2)
		if z8 <= 8:
			z8 = z8+3
			x = d8/5
			x = 4*x
			paths.append(3)
		else:
			x = 6*x
			d8 = d8+z8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))