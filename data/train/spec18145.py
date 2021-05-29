import numpy as np 

def function(x):

	z3 = 3
	y9 = 3
	x = x
	paths = []
	try:
		if x > 4:
			z3 = z3-2
			x = x/3
			x = 5/x
			paths.append(1)
		else:
			y9 = z3/2
			paths.append(2)
		if z3 < 5:
			x = 9*x
			z3 = y9/y9
			x = x*9
			paths.append(3)
		else:
			x = x/z3
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