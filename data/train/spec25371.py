import numpy as np 

def function(x):

	z3 = 3
	n9 = x
	paths = []
	try:
		if n9 <= 3:
			x = x+9
			z3 = 7-z3
			z3 = z3-n9
			paths.append(1)
		else:
			z3 = 6+z3
			x = 1*n9
			n9 = n9/5
			paths.append(2)
		if n9 < 0:
			n9 = x*x
			paths.append(3)
		else:
			n9 = 9*z3
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