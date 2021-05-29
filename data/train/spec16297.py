import numpy as np 

def function(x):

	s0 = x
	z0 = x
	paths = []
	try:
		if s0 <= 0:
			z0 = z0+5
			z0 = 6/8
			paths.append(1)
		else:
			s0 = z0*s0
			paths.append(2)
		if z0 < 9:
			x = z0*s0
			z0 = 5*2
			paths.append(3)
		else:
			z0 = z0-9
			z0 = s0-8
			paths.append(4)
		paths.append(5)
		assert s0 >= 0
		s0 = s0**0.5
		return s0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))