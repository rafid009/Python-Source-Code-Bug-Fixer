import numpy as np 

def function(x):

	s8 = x
	z3 = 8
	paths = []
	try:
		if x >= 8:
			s8 = s8*3
			x = 1*s8
			paths.append(1)
		else:
			z3 = z3/6
			x = 6/x
			z3 = x/z3
			paths.append(2)
		if x >= 3:
			s8 = 9-z3
			paths.append(3)
		else:
			z3 = z3/z3
			paths.append(4)
		paths.append(5)
		assert s8 >= 0
		s8 = s8**0.5
		return s8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))