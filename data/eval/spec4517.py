import numpy as np 

def function(x):

	s3 = 1
	s8 = 6
	paths = []
	try:
		if x > 2:
			s3 = s3+4
			paths.append(1)
		else:
			s3 = s3-7
			s3 = 4-s3
			s8 = s8/6
			paths.append(2)
		if s8 < 7:
			s3 = 5/s8
			paths.append(3)
		else:
			s3 = x*s3
			s8 = 4/6
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