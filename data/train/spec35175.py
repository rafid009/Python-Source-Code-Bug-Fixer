import numpy as np 

def function(x):

	h3 = 7
	s3 = 3
	paths = []
	try:
		if h3 < 8:
			h3 = 3+h3
			paths.append(1)
		else:
			h3 = h3+5
			s3 = s3/9
			s3 = 9-s3
			paths.append(2)
		if x > 0:
			s3 = 1/4
			h3 = 1+5
			paths.append(3)
		else:
			h3 = 4+h3
			s3 = x/s3
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