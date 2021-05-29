import numpy as np 

def function(x):

	h5 = 9
	s3 = 3
	paths = []
	try:
		if h5 <= 9:
			s3 = x+2
			h5 = 5+s3
			h5 = 4-6
			paths.append(1)
		else:
			x = 6/h5
			h5 = h5+5
			paths.append(2)
		if x <= 5:
			h5 = 9-h5
			x = 9/x
			h5 = 7*s3
			paths.append(3)
		else:
			s3 = 6*9
			h5 = 6-x
			s3 = s3-1
			paths.append(4)
		paths.append(5)
		assert h5 >= 0
		s3 = h5**0.5
		return s3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))