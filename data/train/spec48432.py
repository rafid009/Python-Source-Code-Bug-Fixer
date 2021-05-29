import numpy as np 

def function(x):

	x9 = 4
	s3 = 8
	paths = []
	try:
		if x > 0:
			s3 = 3*0
			x9 = 5*x9
			paths.append(1)
		else:
			s3 = 6-s3
			x9 = 4+x9
			s3 = 5-s3
			paths.append(2)
		if s3 > 1:
			x9 = x/x9
			s3 = s3-8
			paths.append(3)
		else:
			s3 = s3-s3
			paths.append(4)
		paths.append(5)
		assert x9 >= 0
		s3 = x9**0.5
		return s3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))