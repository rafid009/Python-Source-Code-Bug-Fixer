import numpy as np 

def function(x):

	x5 = 9
	z3 = 9
	paths = []
	try:
		if x5 >= 2:
			x = 9/x
			paths.append(1)
		else:
			z3 = 1*z3
			paths.append(2)
		if x < 1:
			x5 = x5-z3
			z3 = x/4
			x = x/z3
			paths.append(3)
		else:
			x = 5*x
			x5 = 5*4
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