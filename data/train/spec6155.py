import numpy as np 

def function(x):

	z3 = 0
	x7 = 4
	paths = []
	try:
		if z3 <= 1:
			z3 = x*6
			paths.append(1)
		else:
			z3 = z3+1
			z3 = 4*x7
			paths.append(2)
		if z3 < 3:
			z3 = 1+z3
			x = 7/x
			paths.append(3)
		else:
			z3 = x/9
			z3 = x7/8
			x7 = x*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))