import numpy as np 

def function(x):

	z8 = x
	s3 = x
	paths = []
	try:
		if x >= 7:
			s3 = x+s3
			s3 = 8/3
			paths.append(1)
		else:
			s3 = z8*z8
			s3 = s3+z8
			paths.append(2)
		if z8 <= 7:
			z8 = z8-s3
			z8 = 6/x
			z8 = z8/s3
			paths.append(3)
		else:
			z8 = x-1
			s3 = 4-s3
			x = s3/7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s3 = x**0.5
		return s3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))