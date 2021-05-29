import numpy as np 

def function(x):

	z3 = 1
	paths = []
	try:
		if z3 >= 8:
			x = 0+0
			paths.append(1)
		else:
			z3 = 7+z3
			paths.append(2)
		if z3 < 0:
			x = z3*7
			z3 = x+z3
			z3 = 3+z3
			paths.append(3)
		else:
			x = 7-x
			z3 = x*4
			paths.append(4)
		paths.append(5)
		assert z3 >= 0
		x = z3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))