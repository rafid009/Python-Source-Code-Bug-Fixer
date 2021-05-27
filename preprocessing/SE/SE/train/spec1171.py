import numpy as np 

def function(x):

	z3 = 1
	z2 = x
	paths = []
	try:
		if z3 > 1:
			z2 = 5/z2
			paths.append(1)
		else:
			z3 = z3+z3
			paths.append(2)
		if z3 <= 7:
			z2 = z2-7
			z2 = z2+z2
			paths.append(3)
		else:
			z3 = z3/z3
			z2 = z3*z3
			z3 = z3+z3
			paths.append(4)
		paths.append(5)
		assert z2 >= 0
		x = z2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))