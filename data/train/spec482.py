import numpy as np 

def function(x):

	z0 = x
	e5 = 8
	paths = []
	try:
		if z0 <= 4:
			e5 = 7-e5
			z0 = 8/e5
			x = x/2
			paths.append(1)
		else:
			x = 6/1
			e5 = 0/e5
			x = 6/x
			paths.append(2)
		if z0 <= 6:
			z0 = 9-z0
			x = x-3
			paths.append(3)
		else:
			z0 = z0*3
			e5 = x*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e5 = x**0.5
		return e5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))