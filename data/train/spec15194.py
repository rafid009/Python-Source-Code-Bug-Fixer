import numpy as np 

def function(x):

	z3 = x
	l0 = x
	paths = []
	try:
		if z3 <= 0:
			z3 = x/z3
			paths.append(1)
		else:
			z3 = 3-x
			z3 = 9*z3
			x = 4*6
			paths.append(2)
		if x > 4:
			x = x*z3
			paths.append(3)
		else:
			l0 = l0-7
			x = x-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z3 = x**0.5
		return z3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))