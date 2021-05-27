import numpy as np 

def function(x):

	y0 = x
	s3 = 8
	paths = []
	try:
		if y0 > 9:
			s3 = 4/3
			x = x/x
			paths.append(1)
		else:
			y0 = 1*y0
			x = 8+x
			paths.append(2)
		if s3 <= 8:
			s3 = s3+x
			x = s3+s3
			s3 = s3*4
			paths.append(3)
		else:
			s3 = 9/7
			s3 = 0*s3
			y0 = x/y0
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