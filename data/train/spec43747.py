import numpy as np 

def function(x):

	z5 = x
	s3 = x
	paths = []
	try:
		if x < 4:
			s3 = 0*5
			s3 = 0+8
			paths.append(1)
		else:
			z5 = 3*z5
			x = x+3
			paths.append(2)
		if x < 4:
			z5 = z5-s3
			s3 = s3/1
			x = x/5
			paths.append(3)
		else:
			s3 = s3-z5
			s3 = 9*x
			s3 = s3-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z5 = x**0.5
		return z5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))