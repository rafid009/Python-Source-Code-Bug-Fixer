import numpy as np 

def function(x):

	z3 = x
	y8 = 9
	x = x
	paths = []
	try:
		if y8 > 7:
			z3 = 1*z3
			paths.append(1)
		else:
			x = y8+x
			paths.append(2)
		if z3 > 5:
			y8 = x-8
			y8 = 1+y8
			paths.append(3)
		else:
			z3 = z3/1
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