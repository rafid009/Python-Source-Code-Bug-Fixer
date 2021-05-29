import numpy as np 

def function(x):

	z3 = x
	a4 = 1
	x = x
	paths = []
	try:
		if x >= 6:
			a4 = z3-1
			paths.append(1)
		else:
			z3 = 7/z3
			paths.append(2)
		if a4 >= 5:
			a4 = a4-4
			a4 = 2+5
			x = x/1
			paths.append(3)
		else:
			x = 2-7
			x = a4/5
			x = z3+x
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