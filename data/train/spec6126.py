import numpy as np 

def function(x):

	i0 = x
	z3 = 9
	paths = []
	try:
		if z3 > 0:
			i0 = 7-4
			paths.append(1)
		else:
			i0 = i0/i0
			z3 = 6*z3
			x = 3/x
			paths.append(2)
		if z3 > 7:
			x = 9/x
			z3 = z3*z3
			x = x-1
			paths.append(3)
		else:
			z3 = 5/z3
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