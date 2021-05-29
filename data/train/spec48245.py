import numpy as np 

def function(x):

	v0 = 4
	z3 = x
	paths = []
	try:
		if v0 <= 8:
			v0 = 1*z3
			paths.append(1)
		else:
			v0 = 8+3
			paths.append(2)
		if v0 >= 7:
			z3 = 9*1
			x = 6-x
			paths.append(3)
		else:
			v0 = x/7
			z3 = z3+z3
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