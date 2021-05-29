import numpy as np 

def function(x):

	z3 = 0
	s6 = 6
	paths = []
	try:
		if z3 <= 9:
			s6 = 9/x
			z3 = 5+z3
			paths.append(1)
		else:
			s6 = s6*2
			x = x*9
			x = 8+7
			paths.append(2)
		if z3 > 1:
			s6 = s6/z3
			z3 = 8+z3
			paths.append(3)
		else:
			z3 = z3/3
			x = x+3
			paths.append(4)
		paths.append(5)
		assert s6 >= 0
		s6 = s6**0.5
		return s6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))