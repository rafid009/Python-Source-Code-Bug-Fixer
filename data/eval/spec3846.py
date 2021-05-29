import numpy as np 

def function(x):

	z3 = 2
	e0 = x
	paths = []
	try:
		if z3 <= 9:
			z3 = e0*1
			z3 = z3-8
			e0 = 3/e0
			paths.append(1)
		else:
			z3 = e0+z3
			paths.append(2)
		if x <= 1:
			x = 6/z3
			z3 = z3-2
			z3 = z3-4
			paths.append(3)
		else:
			e0 = 9/9
			e0 = e0*8
			e0 = 7+e0
			paths.append(4)
		paths.append(5)
		assert e0 >= 0
		x = e0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))