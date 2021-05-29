import numpy as np 

def function(x):

	z3 = 6
	e4 = 8
	paths = []
	try:
		if z3 >= 5:
			z3 = z3*e4
			paths.append(1)
		else:
			x = x/6
			x = 1*7
			e4 = x-z3
			paths.append(2)
		if z3 > 3:
			e4 = 9-e4
			z3 = z3*5
			z3 = 2-5
			paths.append(3)
		else:
			e4 = e4*7
			z3 = z3/8
			z3 = 4/5
			paths.append(4)
		paths.append(5)
		assert z3 >= 0
		z3 = z3**0.5
		return z3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))