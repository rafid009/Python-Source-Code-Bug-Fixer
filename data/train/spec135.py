import numpy as np 

def function(x):

	z3 = x
	f1 = 4
	x = x
	paths = []
	try:
		if z3 > 4:
			z3 = z3-7
			x = x*5
			paths.append(1)
		else:
			z3 = 1*f1
			paths.append(2)
		if z3 < 2:
			z3 = f1/z3
			paths.append(3)
		else:
			z3 = x/5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f1 = x**0.5
		return f1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))