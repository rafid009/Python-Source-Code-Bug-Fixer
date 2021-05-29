import numpy as np 

def function(x):

	z0 = 1
	s5 = 8
	paths = []
	try:
		if z0 < 9:
			s5 = 6-s5
			x = 6-x
			s5 = 5-1
			paths.append(1)
		else:
			z0 = 4+s5
			s5 = 8+x
			z0 = 5*z0
			paths.append(2)
		if s5 <= 3:
			x = 1*7
			paths.append(3)
		else:
			z0 = 4/z0
			x = 5/x
			z0 = 3/7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z0 = x**0.5
		return z0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))