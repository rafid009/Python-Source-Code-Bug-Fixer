import numpy as np 

def function(x):

	z3 = x
	o7 = 0
	paths = []
	try:
		if o7 >= 7:
			x = o7*x
			paths.append(1)
		else:
			o7 = o7-7
			z3 = z3*4
			paths.append(2)
		if x <= 2:
			z3 = z3+o7
			paths.append(3)
		else:
			o7 = 3*2
			z3 = z3/z3
			paths.append(4)
		paths.append(5)
		assert o7 >= 0
		x = o7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))