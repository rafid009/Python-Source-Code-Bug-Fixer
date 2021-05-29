import numpy as np 

def function(x):

	i0 = x
	z8 = x
	paths = []
	try:
		if i0 <= 2:
			x = x-3
			z8 = 5+z8
			paths.append(1)
		else:
			i0 = 4-i0
			z8 = z8/7
			paths.append(2)
		if z8 > 6:
			z8 = z8/2
			paths.append(3)
		else:
			x = x-6
			z8 = i0-z8
			x = 2-0
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