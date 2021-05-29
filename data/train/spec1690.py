import numpy as np 

def function(x):

	z2 = 8
	s1 = 1
	paths = []
	try:
		if x <= 0:
			x = x*7
			z2 = 3*5
			paths.append(1)
		else:
			x = 0-x
			s1 = s1*5
			paths.append(2)
		if z2 < 0:
			z2 = z2/s1
			paths.append(3)
		else:
			z2 = z2/z2
			z2 = z2*5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s1 = x**0.5
		return s1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))