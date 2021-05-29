import numpy as np 

def function(x):

	z3 = 7
	t8 = 6
	paths = []
	try:
		if z3 >= 0:
			t8 = 1-t8
			paths.append(1)
		else:
			x = x-9
			z3 = z3+3
			paths.append(2)
		if z3 < 8:
			x = x/t8
			paths.append(3)
		else:
			t8 = t8/6
			t8 = t8*z3
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