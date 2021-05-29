import numpy as np 

def function(x):

	v3 = x
	z3 = x
	paths = []
	try:
		if z3 > 6:
			z3 = z3+5
			paths.append(1)
		else:
			z3 = v3*7
			paths.append(2)
		if v3 > 1:
			z3 = z3+z3
			paths.append(3)
		else:
			z3 = 4-z3
			x = 3*x
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