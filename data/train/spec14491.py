import numpy as np 

def function(x):

	s6 = 7
	z0 = 1
	x = 0
	paths = []
	try:
		if z0 < 8:
			s6 = s6-3
			paths.append(1)
		else:
			z0 = z0+9
			z0 = 8+z0
			paths.append(2)
		if z0 > 9:
			z0 = 6/s6
			z0 = z0*x
			paths.append(3)
		else:
			s6 = x+9
			s6 = z0-s6
			x = 9+x
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