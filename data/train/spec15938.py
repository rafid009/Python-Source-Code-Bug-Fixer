import numpy as np 

def function(x):

	q7 = x
	z3 = 2
	paths = []
	try:
		if x < 3:
			x = 9/x
			z3 = 5-z3
			q7 = q7-8
			paths.append(1)
		else:
			x = 0/x
			x = 9*4
			paths.append(2)
		if z3 >= 0:
			z3 = z3-5
			x = x*5
			z3 = x+z3
			paths.append(3)
		else:
			x = 8-x
			z3 = z3*q7
			z3 = 0-9
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