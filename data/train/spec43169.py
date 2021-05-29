import numpy as np 

def function(x):

	z3 = 1
	r1 = 8
	paths = []
	try:
		if z3 < 8:
			z3 = x-4
			paths.append(1)
		else:
			r1 = x/3
			paths.append(2)
		if r1 >= 9:
			x = x-2
			z3 = 8/8
			x = x-0
			paths.append(3)
		else:
			r1 = 3-1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r1 = x**0.5
		return r1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))