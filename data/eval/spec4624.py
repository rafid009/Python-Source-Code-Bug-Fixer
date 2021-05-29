import numpy as np 

def function(x):

	z3 = 0
	b7 = 4
	paths = []
	try:
		if z3 > 6:
			b7 = 6-5
			paths.append(1)
		else:
			z3 = z3*b7
			z3 = 3/4
			paths.append(2)
		if z3 > 8:
			z3 = z3+z3
			paths.append(3)
		else:
			b7 = x*b7
			paths.append(4)
		paths.append(5)
		assert b7 >= 0
		z3 = b7**0.5
		return z3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))