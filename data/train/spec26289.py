import numpy as np 

def function(x):

	k1 = 6
	z3 = 7
	paths = []
	try:
		if x < 4:
			z3 = 0-z3
			paths.append(1)
		else:
			z3 = z3*6
			paths.append(2)
		if z3 > 1:
			z3 = z3-z3
			paths.append(3)
		else:
			k1 = k1*z3
			z3 = k1-1
			paths.append(4)
		paths.append(5)
		assert k1 >= 0
		z3 = k1**0.5
		return z3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))