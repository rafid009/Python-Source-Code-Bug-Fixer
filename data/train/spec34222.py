import numpy as np 

def function(x):

	s3 = 3
	x2 = 4
	paths = []
	try:
		if s3 >= 8:
			s3 = x*s3
			paths.append(1)
		else:
			s3 = 1+3
			x2 = 6-x2
			paths.append(2)
		if x2 > 9:
			x = 9/s3
			paths.append(3)
		else:
			s3 = x2-7
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