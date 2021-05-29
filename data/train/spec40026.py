import numpy as np 

def function(x):

	z8 = x
	s8 = x
	paths = []
	try:
		if z8 > 0:
			z8 = 9+z8
			z8 = z8-6
			s8 = 1*s8
			paths.append(1)
		else:
			z8 = z8*4
			paths.append(2)
		if s8 < 3:
			z8 = s8*7
			z8 = 6/x
			paths.append(3)
		else:
			s8 = x+s8
			paths.append(4)
		paths.append(5)
		assert z8 >= 0
		s8 = z8**0.5
		return s8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))