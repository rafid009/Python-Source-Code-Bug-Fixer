import numpy as np 

def function(x):

	a5 = 0
	z0 = x
	paths = []
	try:
		if a5 >= 0:
			a5 = 1*3
			paths.append(1)
		else:
			x = x-8
			paths.append(2)
		if z0 <= 0:
			x = x+x
			paths.append(3)
		else:
			z0 = 6/z0
			z0 = 5/4
			a5 = a5*9
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