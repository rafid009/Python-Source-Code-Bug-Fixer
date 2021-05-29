import numpy as np 

def function(x):

	z3 = 4
	s3 = x
	paths = []
	try:
		if z3 > 9:
			x = x+s3
			paths.append(1)
		else:
			z3 = x-0
			paths.append(2)
		if x <= 0:
			z3 = z3+5
			paths.append(3)
		else:
			s3 = s3*9
			z3 = z3-3
			z3 = z3-6
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