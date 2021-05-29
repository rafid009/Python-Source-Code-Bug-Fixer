import numpy as np 

def function(x):

	z3 = x
	q1 = x
	paths = []
	try:
		if z3 >= 9:
			q1 = q1-q1
			q1 = x-2
			paths.append(1)
		else:
			z3 = z3+z3
			z3 = 3*0
			paths.append(2)
		if z3 <= 1:
			z3 = 5+z3
			paths.append(3)
		else:
			x = x-6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))