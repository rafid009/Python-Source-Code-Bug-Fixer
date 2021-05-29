import numpy as np 

def function(x):

	x2 = 2
	z3 = x
	paths = []
	try:
		if z3 >= 4:
			x = 3*x2
			z3 = 7/1
			paths.append(1)
		else:
			z3 = z3-9
			z3 = 0*z3
			x2 = x2+3
			paths.append(2)
		if x2 > 1:
			x2 = x2-6
			paths.append(3)
		else:
			x = x+0
			z3 = z3-7
			z3 = z3-x2
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