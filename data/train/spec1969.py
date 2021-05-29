import numpy as np 

def function(x):

	l6 = 1
	z3 = 6
	paths = []
	try:
		if z3 < 7:
			z3 = 3+z3
			l6 = l6*3
			l6 = l6/l6
			paths.append(1)
		else:
			l6 = 8-l6
			l6 = 7-3
			paths.append(2)
		if l6 < 5:
			l6 = 2-1
			paths.append(3)
		else:
			x = z3+x
			z3 = 9-z3
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