import numpy as np 

def function(x):

	s3 = x
	h2 = 1
	paths = []
	try:
		if s3 >= 1:
			x = x/h2
			paths.append(1)
		else:
			x = x-s3
			paths.append(2)
		if s3 < 4:
			h2 = h2*9
			s3 = 4-s3
			s3 = s3-x
			paths.append(3)
		else:
			h2 = s3/s3
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