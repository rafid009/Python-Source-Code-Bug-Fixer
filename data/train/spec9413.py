import numpy as np 

def function(x):

	x2 = 9
	z3 = 3
	paths = []
	try:
		if x <= 2:
			x2 = x2*z3
			x = 1-2
			x = 9-x
			paths.append(1)
		else:
			z3 = z3-6
			z3 = 5*6
			paths.append(2)
		if x <= 2:
			x = 8/x
			x2 = 5-x
			paths.append(3)
		else:
			z3 = 5-z3
			z3 = z3-6
			x = x+6
			paths.append(4)
		paths.append(5)
		assert z3 >= 0
		x2 = z3**0.5
		return x2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))