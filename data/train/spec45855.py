import numpy as np 

def function(x):

	y0 = 5
	s3 = x
	paths = []
	try:
		if s3 >= 6:
			y0 = 7/s3
			y0 = y0-s3
			y0 = y0/y0
			paths.append(1)
		else:
			s3 = y0*s3
			paths.append(2)
		if x > 1:
			y0 = 7-y0
			s3 = 0-s3
			y0 = 9*s3
			paths.append(3)
		else:
			s3 = x/s3
			s3 = 7+s3
			y0 = x+y0
			paths.append(4)
		paths.append(5)
		assert s3 >= 0
		s3 = s3**0.5
		return s3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))