import numpy as np 

def function(x):

	z3 = x
	b8 = x
	paths = []
	try:
		if z3 >= 5:
			x = x-x
			paths.append(1)
		else:
			z3 = 7-z3
			b8 = x/6
			z3 = x*7
			paths.append(2)
		if b8 < 6:
			b8 = z3-b8
			b8 = 0-b8
			paths.append(3)
		else:
			x = 7*x
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