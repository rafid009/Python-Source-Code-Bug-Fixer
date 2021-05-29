import numpy as np 

def function(x):

	p8 = x
	z3 = 0
	paths = []
	try:
		if x > 3:
			x = 8+z3
			paths.append(1)
		else:
			p8 = p8+z3
			x = x/9
			z3 = z3-p8
			paths.append(2)
		if z3 < 5:
			z3 = z3*x
			paths.append(3)
		else:
			p8 = p8+7
			p8 = 3+z3
			z3 = z3*4
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