import numpy as np 

def function(x):

	s3 = 1
	h8 = 6
	paths = []
	try:
		if h8 < 3:
			s3 = s3+8
			paths.append(1)
		else:
			h8 = h8+1
			s3 = s3+h8
			paths.append(2)
		if h8 > 1:
			s3 = 3/s3
			s3 = 3*7
			s3 = s3/8
			paths.append(3)
		else:
			x = 0/1
			h8 = 8/h8
			h8 = 6/h8
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