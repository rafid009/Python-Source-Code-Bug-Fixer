import numpy as np 

def function(x):

	a2 = x
	z3 = x
	paths = []
	try:
		if a2 < 7:
			x = x+4
			a2 = 8-a2
			paths.append(1)
		else:
			z3 = z3-4
			z3 = a2*9
			z3 = x-z3
			paths.append(2)
		if z3 > 7:
			x = 2-x
			x = 1/x
			paths.append(3)
		else:
			a2 = a2-8
			paths.append(4)
		paths.append(5)
		assert a2 >= 0
		z3 = a2**0.5
		return z3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))