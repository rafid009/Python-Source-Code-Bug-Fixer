import numpy as np 

def function(x):

	z3 = 0
	e2 = x
	paths = []
	try:
		if z3 <= 9:
			z3 = z3/1
			x = 6/x
			paths.append(1)
		else:
			e2 = e2/x
			z3 = z3*4
			paths.append(2)
		if z3 > 7:
			z3 = 6*x
			x = 2*0
			paths.append(3)
		else:
			x = x+1
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