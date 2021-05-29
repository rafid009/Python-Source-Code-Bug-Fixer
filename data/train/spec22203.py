import numpy as np 

def function(x):

	x8 = 3
	z3 = 9
	paths = []
	try:
		if z3 <= 7:
			z3 = z3/7
			x8 = x8*8
			paths.append(1)
		else:
			x8 = 9*x8
			x8 = x8-8
			paths.append(2)
		if x > 9:
			x8 = x8-9
			paths.append(3)
		else:
			x8 = 0-x8
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