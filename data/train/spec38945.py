import numpy as np 

def function(x):

	n8 = x
	z3 = 3
	x = 9
	paths = []
	try:
		if n8 < 6:
			x = n8*x
			paths.append(1)
		else:
			x = x/9
			z3 = z3*z3
			paths.append(2)
		if n8 < 0:
			x = 1/x
			n8 = n8*n8
			paths.append(3)
		else:
			z3 = 4+0
			z3 = 3-z3
			paths.append(4)
		paths.append(5)
		assert z3 >= 0
		n8 = z3**0.5
		return n8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))