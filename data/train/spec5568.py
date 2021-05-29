import numpy as np 

def function(x):

	h8 = 2
	s3 = x
	paths = []
	try:
		if s3 > 0:
			s3 = 9+1
			s3 = s3*4
			s3 = 4-2
			paths.append(1)
		else:
			h8 = 3-s3
			paths.append(2)
		if s3 > 4:
			x = x*x
			s3 = s3+s3
			paths.append(3)
		else:
			s3 = s3-7
			x = 4-8
			s3 = s3+1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h8 = x**0.5
		return h8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))