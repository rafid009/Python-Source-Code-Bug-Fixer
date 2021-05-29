import numpy as np 

def function(x):

	z3 = x
	a3 = 7
	paths = []
	try:
		if a3 <= 5:
			a3 = a3-5
			z3 = 0-4
			paths.append(1)
		else:
			z3 = z3+3
			paths.append(2)
		if x >= 7:
			a3 = a3*5
			z3 = 7+z3
			paths.append(3)
		else:
			a3 = 6/5
			z3 = 8-9
			a3 = 2*z3
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