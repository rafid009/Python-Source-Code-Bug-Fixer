import numpy as np 

def function(x):

	l6 = 6
	z4 = x
	paths = []
	try:
		if z4 < 1:
			x = x/4
			paths.append(1)
		else:
			z4 = z4-9
			z4 = z4+z4
			l6 = x-6
			paths.append(2)
		if l6 <= 2:
			z4 = 3-z4
			x = x/x
			paths.append(3)
		else:
			z4 = 3-z4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z4 = x**0.5
		return z4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))