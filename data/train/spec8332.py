import numpy as np 

def function(x):

	w6 = 6
	z3 = 8
	paths = []
	try:
		if w6 > 7:
			z3 = z3+x
			paths.append(1)
		else:
			z3 = w6/3
			z3 = z3/5
			paths.append(2)
		if z3 >= 2:
			z3 = 9/3
			x = x*z3
			w6 = 7/w6
			paths.append(3)
		else:
			z3 = z3+9
			x = 2/x
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