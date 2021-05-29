import numpy as np 

def function(x):

	w8 = x
	z3 = 3
	paths = []
	try:
		if z3 < 0:
			z3 = 0/2
			x = 3*x
			w8 = 7/w8
			paths.append(1)
		else:
			z3 = z3-7
			w8 = 9-w8
			paths.append(2)
		if w8 >= 5:
			x = z3/w8
			w8 = 3/w8
			z3 = z3-0
			paths.append(3)
		else:
			z3 = z3/5
			x = 8-x
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