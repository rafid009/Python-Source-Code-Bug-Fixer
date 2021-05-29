import numpy as np 

def function(x):

	z3 = 8
	s9 = 9
	paths = []
	try:
		if x < 6:
			x = x*x
			z3 = z3*8
			paths.append(1)
		else:
			s9 = 4-s9
			paths.append(2)
		if x <= 2:
			z3 = x+x
			paths.append(3)
		else:
			z3 = s9*8
			paths.append(4)
		paths.append(5)
		assert z3 >= 0
		s9 = z3**0.5
		return s9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))