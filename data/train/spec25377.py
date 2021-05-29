import numpy as np 

def function(x):

	e5 = 3
	z0 = 9
	paths = []
	try:
		if z0 > 6:
			e5 = e5+x
			e5 = 3-z0
			z0 = 9*9
			paths.append(1)
		else:
			x = z0/6
			paths.append(2)
		if x > 2:
			x = 5+e5
			z0 = z0+9
			e5 = e5/5
			paths.append(3)
		else:
			x = x*x
			x = x-9
			x = 6+6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z0 = x**0.5
		return z0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))