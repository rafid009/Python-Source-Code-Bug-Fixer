import numpy as np 

def function(x):

	z0 = x
	s3 = x
	paths = []
	try:
		if s3 < 7:
			s3 = 7-4
			x = x*x
			paths.append(1)
		else:
			s3 = 3/x
			paths.append(2)
		if s3 > 6:
			s3 = z0/7
			z0 = 0+s3
			paths.append(3)
		else:
			x = x-6
			z0 = z0/x
			z0 = 8+z0
			paths.append(4)
		paths.append(5)
		assert z0 >= 0
		s3 = z0**0.5
		return s3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))