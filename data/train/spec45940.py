import numpy as np 

def function(x):

	z5 = x
	s1 = 7
	paths = []
	try:
		if z5 < 8:
			s1 = 0*s1
			s1 = 8-s1
			z5 = 6+z5
			paths.append(1)
		else:
			z5 = 4*z5
			z5 = z5/9
			s1 = s1+x
			paths.append(2)
		if x > 4:
			s1 = 1*1
			z5 = 6/z5
			paths.append(3)
		else:
			x = x-3
			z5 = 8*x
			s1 = s1/3
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