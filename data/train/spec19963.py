import numpy as np 

def function(x):

	o4 = x
	z3 = 3
	paths = []
	try:
		if o4 < 4:
			o4 = o4*6
			o4 = o4+z3
			o4 = o4/7
			paths.append(1)
		else:
			o4 = 1*x
			o4 = o4-z3
			paths.append(2)
		if x <= 9:
			o4 = o4*x
			z3 = o4/z3
			z3 = z3-2
			paths.append(3)
		else:
			z3 = z3-x
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