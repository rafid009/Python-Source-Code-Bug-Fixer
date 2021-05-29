import numpy as np 

def function(x):

	l5 = 0
	z3 = 9
	paths = []
	try:
		if z3 >= 9:
			x = 6+x
			l5 = l5/3
			paths.append(1)
		else:
			l5 = z3/7
			paths.append(2)
		if x > 2:
			l5 = l5+4
			z3 = z3-7
			z3 = 6*z3
			paths.append(3)
		else:
			l5 = l5*9
			l5 = l5*9
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