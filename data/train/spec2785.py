import numpy as np 

def function(x):

	a8 = 7
	z3 = x
	paths = []
	try:
		if x < 9:
			x = x*3
			a8 = a8-a8
			paths.append(1)
		else:
			z3 = 8+5
			paths.append(2)
		if z3 <= 9:
			z3 = 9+5
			z3 = 7/z3
			paths.append(3)
		else:
			a8 = z3*8
			z3 = 3-z3
			x = a8/x
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