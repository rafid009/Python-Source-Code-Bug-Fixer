import numpy as np 

def function(x):

	z3 = x
	d6 = x
	paths = []
	try:
		if z3 >= 9:
			z3 = 9-8
			paths.append(1)
		else:
			z3 = d6/z3
			paths.append(2)
		if z3 < 1:
			d6 = z3/z3
			paths.append(3)
		else:
			d6 = 8-x
			x = d6/6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d6 = x**0.5
		return d6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))