import numpy as np 

def function(x):

	w8 = 1
	z3 = 2
	paths = []
	try:
		if x > 0:
			x = 4*x
			x = 2*x
			paths.append(1)
		else:
			w8 = x+6
			paths.append(2)
		if w8 < 8:
			z3 = x*x
			x = x-z3
			paths.append(3)
		else:
			x = 8/x
			x = 5/x
			paths.append(4)
		paths.append(5)
		assert w8 >= 0
		z3 = w8**0.5
		return z3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))