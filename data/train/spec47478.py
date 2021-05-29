import numpy as np 

def function(x):

	s3 = x
	z5 = x
	paths = []
	try:
		if s3 <= 7:
			s3 = 8+x
			s3 = s3+z5
			z5 = s3+x
			paths.append(1)
		else:
			s3 = s3/z5
			z5 = s3/z5
			x = 2+z5
			paths.append(2)
		if x < 8:
			z5 = s3+2
			paths.append(3)
		else:
			x = x-x
			paths.append(4)
		paths.append(5)
		assert z5 >= 0
		x = z5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))