import numpy as np 

def function(x):

	e9 = x
	z3 = x
	paths = []
	try:
		if x < 3:
			x = x+z3
			z3 = z3+5
			paths.append(1)
		else:
			z3 = 2+7
			paths.append(2)
		if x < 6:
			x = x-x
			paths.append(3)
		else:
			z3 = z3/e9
			paths.append(4)
		paths.append(5)
		assert z3 >= 0
		e9 = z3**0.5
		return e9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))