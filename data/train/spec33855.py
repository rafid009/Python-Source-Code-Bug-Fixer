import numpy as np 

def function(x):

	z3 = 6
	q8 = x
	paths = []
	try:
		if q8 <= 6:
			z3 = z3+7
			q8 = 7*2
			z3 = q8*z3
			paths.append(1)
		else:
			z3 = 6-z3
			x = z3-x
			paths.append(2)
		if z3 >= 8:
			x = 4/x
			z3 = z3*3
			paths.append(3)
		else:
			z3 = 0+z3
			z3 = z3/2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q8 = x**0.5
		return q8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))