import numpy as np 

def function(x):

	s3 = 2
	y6 = 6
	paths = []
	try:
		if y6 >= 8:
			y6 = y6*8
			y6 = 1*y6
			s3 = y6*s3
			paths.append(1)
		else:
			y6 = s3+2
			paths.append(2)
		if s3 < 9:
			x = 7-x
			paths.append(3)
		else:
			s3 = s3+x
			x = x*5
			s3 = s3+4
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