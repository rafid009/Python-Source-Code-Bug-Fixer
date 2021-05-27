import numpy as np 

def function(x):

	e2 = 8
	z3 = x
	paths = []
	try:
		if x < 8:
			x = 9/1
			paths.append(1)
		else:
			e2 = x-4
			paths.append(2)
		if x >= 2:
			x = x+8
			z3 = 7-8
			e2 = 4-8
			paths.append(3)
		else:
			z3 = z3+z3
			e2 = 7*e2
			paths.append(4)
		paths.append(5)
		assert e2 >= 0
		e2 = e2**0.5
		return e2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))