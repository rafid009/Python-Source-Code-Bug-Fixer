import numpy as np 

def function(x):

	z2 = 8
	z3 = x
	paths = []
	try:
		if z3 < 1:
			x = 0+x
			z2 = z2+4
			paths.append(1)
		else:
			z2 = z2-4
			z2 = 8-0
			paths.append(2)
		if x > 2:
			z3 = z3+6
			z3 = z3+2
			z2 = z2-4
			paths.append(3)
		else:
			x = 3-x
			z3 = z3/3
			paths.append(4)
		paths.append(5)
		assert z3 >= 0
		z3 = z3**0.5
		return z3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))