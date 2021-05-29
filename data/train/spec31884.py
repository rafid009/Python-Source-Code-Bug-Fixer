import numpy as np 

def function(x):

	z3 = x
	z0 = 3
	paths = []
	try:
		if z0 <= 1:
			z3 = 4+z3
			paths.append(1)
		else:
			z3 = 7/z3
			x = z0/x
			paths.append(2)
		if x < 5:
			x = 2-6
			x = x+2
			paths.append(3)
		else:
			z0 = x+z0
			z3 = x-4
			z3 = z0*z0
			paths.append(4)
		paths.append(5)
		assert z3 >= 0
		z0 = z3**0.5
		return z0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))