import numpy as np 

def function(x):

	l4 = 5
	z0 = 2
	paths = []
	try:
		if z0 < 4:
			z0 = 1-z0
			z0 = z0/z0
			z0 = z0-2
			paths.append(1)
		else:
			z0 = l4-z0
			x = x+9
			paths.append(2)
		if x <= 2:
			x = x/4
			x = x-5
			l4 = 0-0
			paths.append(3)
		else:
			z0 = z0+x
			x = 5-1
			l4 = z0+5
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