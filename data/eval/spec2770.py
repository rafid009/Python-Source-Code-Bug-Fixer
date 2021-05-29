import numpy as np 

def function(x):

	s7 = x
	z0 = 6
	paths = []
	try:
		if s7 < 7:
			z0 = x+z0
			z0 = 4/z0
			paths.append(1)
		else:
			s7 = 0+s7
			z0 = 4*5
			paths.append(2)
		if x >= 0:
			x = x+5
			x = s7+x
			paths.append(3)
		else:
			z0 = 0+4
			x = x+7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s7 = x**0.5
		return s7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))