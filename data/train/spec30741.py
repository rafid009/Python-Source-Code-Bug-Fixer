import numpy as np 

def function(x):

	z3 = x
	y6 = 9
	x = x
	paths = []
	try:
		if z3 <= 8:
			z3 = 4-z3
			x = x/x
			paths.append(1)
		else:
			z3 = z3/3
			x = x/3
			x = z3+0
			paths.append(2)
		if z3 < 7:
			z3 = 3*z3
			x = 6/6
			y6 = 7-y6
			paths.append(3)
		else:
			x = y6/y6
			x = 6*x
			x = 2/x
			paths.append(4)
		paths.append(5)
		assert y6 >= 0
		z3 = y6**0.5
		return z3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))