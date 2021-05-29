import numpy as np 

def function(x):

	z3 = x
	m2 = x
	paths = []
	try:
		if z3 <= 6:
			m2 = 3-m2
			x = x+8
			x = 0-4
			paths.append(1)
		else:
			z3 = z3*z3
			paths.append(2)
		if x < 2:
			m2 = 6/z3
			m2 = m2*6
			z3 = m2-z3
			paths.append(3)
		else:
			z3 = 3*z3
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