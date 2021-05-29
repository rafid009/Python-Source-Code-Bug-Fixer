import numpy as np 

def function(x):

	h5 = x
	s3 = x
	paths = []
	try:
		if s3 <= 2:
			x = x/3
			h5 = 5/h5
			paths.append(1)
		else:
			s3 = 4-2
			x = x-5
			h5 = h5*1
			paths.append(2)
		if x <= 6:
			x = x*x
			paths.append(3)
		else:
			s3 = s3+9
			x = x/h5
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