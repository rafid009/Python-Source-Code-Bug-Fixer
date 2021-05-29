import numpy as np 

def function(x):

	z3 = 3
	s2 = x
	paths = []
	try:
		if s2 >= 7:
			x = 5*x
			s2 = x/2
			z3 = s2-z3
			paths.append(1)
		else:
			z3 = 3+z3
			x = 8+x
			s2 = 4-s2
			paths.append(2)
		if s2 < 2:
			s2 = 1+s2
			paths.append(3)
		else:
			x = x/s2
			z3 = x-2
			s2 = 5-s2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))