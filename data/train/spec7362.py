import numpy as np 

def function(x):

	h3 = x
	z3 = 6
	paths = []
	try:
		if z3 <= 9:
			z3 = z3/5
			h3 = z3/h3
			h3 = h3+3
			paths.append(1)
		else:
			h3 = x/h3
			x = z3/h3
			paths.append(2)
		if h3 >= 4:
			z3 = 1*z3
			x = z3*h3
			z3 = x/7
			paths.append(3)
		else:
			z3 = 1-3
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