import numpy as np 

def function(x):

	q3 = 7
	z3 = x
	paths = []
	try:
		if z3 <= 3:
			q3 = 8*z3
			z3 = x*z3
			paths.append(1)
		else:
			x = x-x
			paths.append(2)
		if q3 < 8:
			z3 = z3*z3
			z3 = 1-2
			paths.append(3)
		else:
			q3 = q3+5
			q3 = z3-0
			q3 = 4*2
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