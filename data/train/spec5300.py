import numpy as np 

def function(x):

	y4 = 9
	s3 = x
	paths = []
	try:
		if s3 < 0:
			y4 = y4*y4
			s3 = s3/3
			x = x/x
			paths.append(1)
		else:
			s3 = x-x
			paths.append(2)
		if x > 8:
			x = x+6
			paths.append(3)
		else:
			s3 = 6*s3
			x = 4+9
			x = y4-9
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