import numpy as np 

def function(x):

	z6 = x
	s3 = 1
	x = x
	paths = []
	try:
		if s3 < 7:
			s3 = z6-7
			x = 4+x
			paths.append(1)
		else:
			s3 = s3*8
			paths.append(2)
		if z6 >= 1:
			s3 = s3*1
			z6 = z6+6
			z6 = z6/3
			paths.append(3)
		else:
			s3 = z6/3
			paths.append(4)
		paths.append(5)
		assert z6 >= 0
		s3 = z6**0.5
		return s3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))