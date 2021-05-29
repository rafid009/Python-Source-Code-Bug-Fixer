import numpy as np 

def function(x):

	b8 = 8
	z3 = 3
	paths = []
	try:
		if x <= 1:
			b8 = 6-z3
			z3 = 4+z3
			paths.append(1)
		else:
			x = 2+x
			paths.append(2)
		if x < 1:
			b8 = 9*x
			z3 = b8-4
			b8 = z3-x
			paths.append(3)
		else:
			x = x-z3
			z3 = 1/b8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b8 = x**0.5
		return b8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))