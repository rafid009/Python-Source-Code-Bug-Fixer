import numpy as np 

def function(x):

	s3 = x
	s2 = x
	paths = []
	try:
		if s2 < 6:
			s3 = s2+7
			s3 = s3-2
			paths.append(1)
		else:
			x = 2+8
			s2 = s2+s2
			s2 = x*s2
			paths.append(2)
		if x > 6:
			s3 = s3*s3
			x = 7-x
			s3 = 8/5
			paths.append(3)
		else:
			s3 = 3*x
			s3 = s3-s2
			s2 = 3*4
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