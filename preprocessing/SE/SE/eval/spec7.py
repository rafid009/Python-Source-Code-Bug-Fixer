import numpy as np 

def function(x):

	z0 = x
	s7 = x
	x = 4
	paths = []
	try:
		if x >= 4:
			z0 = 7-z0
			s7 = s7*s7
			s7 = 0-s7
			paths.append(1)
		else:
			x = x*z0
			x = z0*4
			z0 = 3+x
			paths.append(2)
		if z0 <= 6:
			s7 = s7*2
			paths.append(3)
		else:
			z0 = 5-z0
			z0 = 7+z0
			paths.append(4)
		paths.append(5)
		assert s7 >= 0
		s7 = s7**0.5
		return s7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))