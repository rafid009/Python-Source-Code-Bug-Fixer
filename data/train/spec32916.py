import numpy as np 

def function(x):

	s3 = 6
	z5 = 5
	paths = []
	try:
		if x <= 2:
			z5 = z5/1
			z5 = 1/5
			s3 = 7/1
			paths.append(1)
		else:
			z5 = z5*z5
			paths.append(2)
		if z5 <= 0:
			x = x+z5
			s3 = 7*x
			paths.append(3)
		else:
			z5 = 2-z5
			x = 5-8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))