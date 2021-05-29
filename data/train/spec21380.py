import numpy as np 

def function(x):

	z3 = x
	x3 = 6
	paths = []
	try:
		if x <= 8:
			z3 = 8*x3
			paths.append(1)
		else:
			z3 = 5*z3
			paths.append(2)
		if x3 <= 3:
			x3 = 1*x3
			z3 = z3-0
			x3 = 5-x3
			paths.append(3)
		else:
			x3 = x+9
			z3 = 7-z3
			x3 = x/5
			paths.append(4)
		paths.append(5)
		assert z3 >= 0
		x3 = z3**0.5
		return x3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))