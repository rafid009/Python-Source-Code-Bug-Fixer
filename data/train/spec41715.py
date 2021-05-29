import numpy as np 

def function(x):

	u4 = 6
	z3 = x
	paths = []
	try:
		if u4 > 7:
			u4 = 8/z3
			z3 = 1-z3
			paths.append(1)
		else:
			u4 = 4-x
			z3 = 5+x
			paths.append(2)
		if x > 7:
			u4 = u4*3
			paths.append(3)
		else:
			z3 = z3/6
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