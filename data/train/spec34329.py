import numpy as np 

def function(x):

	s3 = x
	h5 = x
	paths = []
	try:
		if s3 < 8:
			s3 = s3/7
			s3 = s3-7
			x = x-5
			paths.append(1)
		else:
			x = x-1
			s3 = x-x
			paths.append(2)
		if h5 <= 5:
			x = 3/x
			h5 = h5*1
			h5 = s3/h5
			paths.append(3)
		else:
			s3 = h5/9
			h5 = 4-h5
			paths.append(4)
		paths.append(5)
		assert s3 >= 0
		x = s3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))