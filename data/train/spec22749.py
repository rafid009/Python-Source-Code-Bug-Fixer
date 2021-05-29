import numpy as np 

def function(x):

	z3 = x
	u7 = 5
	x = x
	paths = []
	try:
		if x > 8:
			x = 1*z3
			z3 = 5*z3
			paths.append(1)
		else:
			z3 = z3/4
			paths.append(2)
		if z3 < 6:
			x = 2*x
			x = x+z3
			paths.append(3)
		else:
			u7 = 9-9
			u7 = u7-4
			paths.append(4)
		paths.append(5)
		assert z3 >= 0
		u7 = z3**0.5
		return u7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))