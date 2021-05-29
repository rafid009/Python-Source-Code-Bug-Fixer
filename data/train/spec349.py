import numpy as np 

def function(x):

	x2 = 4
	z3 = 7
	paths = []
	try:
		if z3 > 0:
			x2 = x2*1
			paths.append(1)
		else:
			x = 3-x2
			paths.append(2)
		if z3 > 9:
			z3 = z3*8
			x2 = x/x2
			x = x-9
			paths.append(3)
		else:
			z3 = 5*3
			z3 = z3/3
			z3 = x*z3
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