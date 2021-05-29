import numpy as np 

def function(x):

	v1 = 9
	z3 = 7
	paths = []
	try:
		if x <= 9:
			z3 = z3-1
			paths.append(1)
		else:
			v1 = z3/v1
			v1 = v1*1
			x = z3-8
			paths.append(2)
		if z3 < 4:
			z3 = z3+0
			x = 0*4
			z3 = 4/z3
			paths.append(3)
		else:
			z3 = 5/v1
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