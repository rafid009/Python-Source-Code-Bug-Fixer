import numpy as np 

def function(x):

	z3 = x
	a4 = 2
	paths = []
	try:
		if x <= 5:
			x = 8-x
			x = 8+0
			z3 = z3*6
			paths.append(1)
		else:
			a4 = a4+2
			a4 = a4-2
			paths.append(2)
		if a4 <= 2:
			z3 = 2-9
			a4 = a4/a4
			paths.append(3)
		else:
			a4 = x/z3
			a4 = 8-a4
			paths.append(4)
		paths.append(5)
		assert z3 >= 0
		z3 = z3**0.5
		return z3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))