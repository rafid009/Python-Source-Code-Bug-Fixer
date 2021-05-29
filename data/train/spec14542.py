import numpy as np 

def function(x):

	r9 = 2
	s3 = x
	paths = []
	try:
		if s3 > 7:
			s3 = r9-s3
			paths.append(1)
		else:
			s3 = r9/s3
			s3 = s3/4
			x = 9+x
			paths.append(2)
		if x <= 6:
			r9 = r9/8
			x = 6/2
			r9 = s3/r9
			paths.append(3)
		else:
			x = x-1
			r9 = r9+2
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