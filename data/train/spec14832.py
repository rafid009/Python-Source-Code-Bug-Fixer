import numpy as np 

def function(x):

	s3 = x
	t0 = 8
	paths = []
	try:
		if x < 2:
			x = 7*x
			s3 = 3*s3
			paths.append(1)
		else:
			x = 7+9
			s3 = 9-s3
			s3 = s3-3
			paths.append(2)
		if x < 9:
			t0 = t0-4
			s3 = s3+3
			paths.append(3)
		else:
			x = x+8
			t0 = s3/x
			s3 = 1-x
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