import numpy as np 

def function(x):

	o6 = 8
	z8 = x
	paths = []
	try:
		if o6 > 9:
			x = o6-x
			paths.append(1)
		else:
			x = 7/x
			paths.append(2)
		if z8 > 3:
			z8 = 6+z8
			x = x+2
			paths.append(3)
		else:
			x = x+6
			z8 = z8*2
			z8 = z8+2
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