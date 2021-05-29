import numpy as np 

def function(x):

	z3 = 1
	o1 = 0
	paths = []
	try:
		if z3 <= 0:
			z3 = z3-z3
			x = 4+2
			paths.append(1)
		else:
			z3 = o1+5
			o1 = o1-z3
			paths.append(2)
		if z3 >= 0:
			z3 = 8-x
			paths.append(3)
		else:
			x = 2*x
			o1 = 1*6
			o1 = z3/2
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