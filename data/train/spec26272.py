import numpy as np 

def function(x):

	u9 = 8
	s3 = 0
	paths = []
	try:
		if s3 > 0:
			x = 6-x
			s3 = 3*s3
			u9 = u9*s3
			paths.append(1)
		else:
			s3 = s3*8
			s3 = u9-u9
			u9 = x-u9
			paths.append(2)
		if s3 > 9:
			u9 = s3-5
			paths.append(3)
		else:
			u9 = 6*6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u9 = x**0.5
		return u9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))