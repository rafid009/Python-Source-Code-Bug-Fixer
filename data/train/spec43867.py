import numpy as np 

def function(x):

	b8 = 8
	z3 = x
	paths = []
	try:
		if x > 0:
			x = b8-x
			x = 2/6
			z3 = 5*z3
			paths.append(1)
		else:
			b8 = x/5
			z3 = x*1
			z3 = z3*z3
			paths.append(2)
		if x >= 8:
			x = 2-6
			b8 = b8-6
			b8 = 9*1
			paths.append(3)
		else:
			z3 = z3-z3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b8 = x**0.5
		return b8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))