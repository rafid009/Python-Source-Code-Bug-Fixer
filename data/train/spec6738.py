import numpy as np 

def function(x):

	x9 = x
	z3 = 9
	paths = []
	try:
		if z3 > 1:
			z3 = z3+0
			x = z3*x
			z3 = z3/x
			paths.append(1)
		else:
			x9 = 1-x9
			paths.append(2)
		if x9 >= 4:
			x = x*z3
			paths.append(3)
		else:
			x9 = x9*1
			paths.append(4)
		paths.append(5)
		assert z3 >= 0
		x = z3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))