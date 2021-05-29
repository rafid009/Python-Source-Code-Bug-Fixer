import numpy as np 

def function(x):

	z3 = 9
	s7 = 0
	paths = []
	try:
		if z3 > 9:
			z3 = 8*z3
			z3 = 7*z3
			paths.append(1)
		else:
			z3 = z3+x
			s7 = 2-1
			paths.append(2)
		if z3 <= 4:
			s7 = z3-z3
			z3 = 4*7
			x = x*5
			paths.append(3)
		else:
			s7 = s7*x
			z3 = 4+z3
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